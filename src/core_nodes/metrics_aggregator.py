"""
Metrics Aggregator for tracking LLM usage across multiple agent calls
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from datetime import datetime

from src.models.llm_metrics import LLMMetrics


@dataclass
class AgentMetrics:
    """Metrics for a specific agent"""
    agent_name: str
    calls: List[LLMMetrics] = field(default_factory=list)
    
    def add_call(self, metrics: LLMMetrics):
        """Add metrics from a single call"""
        self.calls.append(metrics)
    
    def get_summary(self) -> Dict[str, Any]:
        """Get summary statistics for this agent"""
        if not self.calls:
            return {
                "agent_name": self.agent_name,
                "total_calls": 0,
                "total_cost": 0.0,
                "total_tokens": 0,
                "avg_response_time_ms": 0.0
            }
        
        total_cost = sum(m.total_cost for m in self.calls)
        total_tokens = sum(m.total_tokens for m in self.calls)
        total_input_tokens = sum(m.input_tokens for m in self.calls)
        total_output_tokens = sum(m.output_tokens for m in self.calls)
        avg_response_time = sum(m.response_time_ms for m in self.calls) / len(self.calls)
        
        return {
            "agent_name": self.agent_name,
            "total_calls": len(self.calls),
            "total_cost": total_cost,
            "total_tokens": total_tokens,
            "total_input_tokens": total_input_tokens,
            "total_output_tokens": total_output_tokens,
            "avg_response_time_ms": avg_response_time,
            "min_response_time_ms": min(m.response_time_ms for m in self.calls),
            "max_response_time_ms": max(m.response_time_ms for m in self.calls),
        }


class MetricsAggregator:
    """Aggregate metrics across multiple agents and calls"""
    
    def __init__(self):
        self.agents: Dict[str, AgentMetrics] = {}
        self.start_time = datetime.now()
    
    def add_metrics(self, agent_name: str, metrics: LLMMetrics):
        """Add metrics for a specific agent call"""
        if agent_name not in self.agents:
            self.agents[agent_name] = AgentMetrics(agent_name)
        self.agents[agent_name].add_call(metrics)
    
    def get_agent_summary(self, agent_name: str) -> Optional[Dict[str, Any]]:
        """Get summary for a specific agent"""
        if agent_name in self.agents:
            return self.agents[agent_name].get_summary()
        return None
    
    def get_summary(self) -> Dict[str, Any]:
        """Get overall summary of all metrics"""
        if not self.agents:
            return {
                "total_agents": 0,
                "total_calls": 0,
                "total_cost": 0.0,
                "total_tokens": 0,
                "duration_seconds": (datetime.now() - self.start_time).total_seconds()
            }
        
        agent_summaries = [agent.get_summary() for agent in self.agents.values()]
        
        total_calls = sum(s["total_calls"] for s in agent_summaries)
        total_cost = sum(s["total_cost"] for s in agent_summaries)
        total_tokens = sum(s["total_tokens"] for s in agent_summaries)
        total_input_tokens = sum(s["total_input_tokens"] for s in agent_summaries)
        total_output_tokens = sum(s["total_output_tokens"] for s in agent_summaries)
        
        # Calculate weighted average response time
        weighted_sum = sum(s["avg_response_time_ms"] * s["total_calls"] for s in agent_summaries)
        avg_response_time = weighted_sum / total_calls if total_calls > 0 else 0
        
        return {
            "total_agents": len(self.agents),
            "total_calls": total_calls,
            "total_cost": total_cost,
            "total_tokens": total_tokens,
            "total_input_tokens": total_input_tokens,
            "total_output_tokens": total_output_tokens,
            "avg_response_time_ms": avg_response_time,
            "duration_seconds": (datetime.now() - self.start_time).total_seconds(),
            "agents": agent_summaries
        }
    
    def get_total_cost(self) -> float:
        """Get total cost across all agents"""
        return sum(
            sum(m.total_cost for m in agent.calls)
            for agent in self.agents.values()
        )
    
    def get_average_latency(self) -> float:
        """Get average latency across all calls"""
        all_calls = []
        for agent in self.agents.values():
            all_calls.extend(agent.calls)
        
        if not all_calls:
            return 0.0
        
        return sum(m.response_time_ms for m in all_calls) / len(all_calls)
    
    def format_summary(self) -> str:
        """Format summary as a readable string"""
        summary = self.get_summary()
        
        lines = [
            "=" * 60,
            "METRICS SUMMARY",
            "=" * 60,
            f"Total Agents: {summary['total_agents']}",
            f"Total API Calls: {summary['total_calls']}",
            f"Total Cost: ${summary['total_cost']:.6f}",
            f"Total Tokens: {summary['total_tokens']:,}",
            f"  - Input: {summary['total_input_tokens']:,}",
            f"  - Output: {summary['total_output_tokens']:,}",
            f"Avg Response Time: {summary['avg_response_time_ms']:.0f}ms",
            f"Duration: {summary['duration_seconds']:.2f}s",
            "-" * 60,
            "PER AGENT BREAKDOWN:",
        ]
        
        for agent_summary in summary["agents"]:
            lines.extend([
                f"\n{agent_summary['agent_name']}:",
                f"  Calls: {agent_summary['total_calls']}",
                f"  Cost: ${agent_summary['total_cost']:.6f}",
                f"  Tokens: {agent_summary['total_tokens']:,}",
                f"  Avg Time: {agent_summary['avg_response_time_ms']:.0f}ms",
            ])
        
        lines.append("=" * 60)
        
        return "\n".join(lines)