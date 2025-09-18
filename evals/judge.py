"""
LLM-as-a-Judge implementation for semantic evaluation.
"""

from typing import Any, Dict, List, Optional
from dataclasses import dataclass


@dataclass
class JudgeResult:
    """Result from LLM judge evaluation."""
    passed: bool
    rationale: Optional[str] = None


class LLMJudge:
    """
    LLM-as-a-Judge for evaluating outputs against semantic criteria.
    
    This uses the provided LLM client interface for evaluation.
    """
    
    def __init__(self, llm_client: Any, temperature: float = 0.1, max_tokens: int = 500):
        """
        Initialize the LLM judge.
        
        Args:
            llm_client: LLM client implementing the LLMClientInterface
            temperature: Temperature for LLM generation
            max_tokens: Maximum tokens for response
        """
        self.llm_client: Any = llm_client
        self.temperature: float = temperature
        self.max_tokens: int = max_tokens
    
    
    async def evaluate(
        self,
        output: str,
        criteria: List[str],
        context: Optional[Dict[str, Any]] = None
    ) -> JudgeResult:
        """
        Evaluate output against specified criteria.
        
        Args:
            output: The output to evaluate
            criteria: List of criteria that must ALL be met
            context: Optional context for evaluation
            
        Returns:
            JudgeResult with pass/fail and rationale
        """
        # Format criteria as numbered list
        criteria_text: str = "\n".join(
            f"{i+1}. {criterion}" for i, criterion in enumerate(criteria)
        )
        
        # Build context section if provided
        context_section: str = ""
        if context:
            context_items: List[str] = []
            for key, value in context.items():
                context_items.append(f"\n{key.upper()}:\n{value}")
            context_section = "\n".join(context_items)
        
        # Create evaluation prompt
        system_prompt: str = """You are a precise and objective evaluator. Your task is to evaluate whether a given output meets ALL specified criteria.

Respond in the following format:
EVALUATION: PASS or FAIL
RATIONALE: (Only if FAIL) Brief explanation of which criteria were not met and why"""
        
        user_prompt: str = f"""Evaluate the following output against the provided criteria.

CRITERIA (ALL must be met for PASS):
{criteria_text}

OUTPUT TO EVALUATE:
{output}{context_section}

Remember: The output must meet ALL criteria to PASS. If ANY criterion is not met, it must FAIL."""
        
        try:
            # Call LLM client
            llm_response = await self.llm_client.generate(
                system_prompt=system_prompt,
                user_prompt=user_prompt,
                temperature=self.temperature,
                max_tokens=self.max_tokens
            )

            # Extract text from LLM response
            response_text: str = llm_response.text if hasattr(llm_response, 'text') else str(llm_response)

            # Parse response
            result: JudgeResult = self._parse_response(response_text)
            return result
            
        except Exception as e:
            # Return failure if evaluation fails
            result: JudgeResult = JudgeResult(
                passed=False,
                rationale=f"LLM evaluation failed: {str(e)}"
            )
            return result
    
    
    def _parse_response(self, response: str) -> JudgeResult:
        """
        Parse the LLM response into a JudgeResult.
        
        Args:
            response: Raw LLM response
            
        Returns:
            Parsed JudgeResult
        """
        lines: List[str] = response.strip().split('\n')
        
        # Default values
        passed: bool = False
        rationale: Optional[str] = None
        
        for line in lines:
            line_upper: str = line.upper()
            
            if "EVALUATION:" in line_upper:
                if "PASS" in line_upper:
                    passed = True
                elif "FAIL" in line_upper:
                    passed = False
            
            elif "RATIONALE:" in line:
                # Extract rationale
                rationale_start: int = line.find("RATIONALE:") + len("RATIONALE:")
                rationale = line[rationale_start:].strip()
                
                # If rationale continues on next lines, collect them
                current_idx: int = lines.index(line)
                for next_line in lines[current_idx + 1:]:
                    if not any(keyword in next_line.upper() 
                              for keyword in ["EVALUATION:", "CRITERIA:", "OUTPUT:"]):
                        rationale += " " + next_line.strip()
                    else:
                        break
        
        # Clean up rationale
        if rationale and not rationale.strip():
            rationale = None
        
        result: JudgeResult = JudgeResult(passed=passed, rationale=rationale)
        return result