import re
from typing import Any, Dict, List, Optional


def get_xml_tag_content(xml_string: str, tag_name: str) -> str:
        """
        Extracts the content of a single XML-like tag.
        
        Args:
            xml_string (str): The input XML-like string.
            tag_name (str): The name of the tag to extract content for.
        
        Returns:
            str: The content inside the specified tag, or an empty string if not found.
        """
        tag_match: Optional[re.Match] = re.search(rf"<{tag_name}>(.*?)</{tag_name}>", xml_string, re.DOTALL)
        if tag_match:
            tag_content: str = tag_match.group(1).strip()
            return tag_content
        else:
            return ""


def parse_object(xml_string: str, field_tags: List[str]) -> Dict[str, str]:
    """
    Parses a single object by extracting its fields based on specified field tags.
    
    Args:
        xml_string (str): The input XML-like string representing a single object.
        field_tags (List[str]): A list of field tag names to extract.
    
    Returns:
        Dict[str, str]: A dictionary representing the object's fields and their values.
    """
    object_dict: Dict[str, str] = {tag: get_xml_tag_content(xml_string, tag) for tag in field_tags}
    return object_dict


def parse_list_of_objects(xml_string: str, object_tag: str, field_tags: List[str]) -> List[Dict[str, str]]:
    """
    Parses a list of objects by extracting all occurrences of an object tag 
    and parsing their fields.
    
    Args:
        xml_string (str): The input XML-like string containing multiple objects.
        object_tag (str): The name of the tag representing a single object.
        field_tags (List[str]): A list of field tag names to extract for each object.
    
    Returns:
        List[Dict[str, str]]: A list of dictionaries representing the parsed objects.
    """
    # Match all occurrences of the object tag
    object_matches: List[str] = re.findall(rf"<{object_tag}>(.*?)</{object_tag}>", xml_string, re.DOTALL)
    # Parse each object using parse_object
    objects: List[Dict[str, str]] = [parse_object(obj, field_tags) for obj in object_matches]
    return objects


def parse_list_of_elements(xml_string: str, object_tag: str, element_tag: str) -> List[str]:
    """
    Parses a list of elements by extracting all occurrences of an element tag 
    within an object tag.
    
    Args:
        xml_string (str): The input XML-like string containing multiple elements.
        object_tag (str): The name of the tag representing the container object.
        element_tag (str): The name of the tag representing individual elements.
    
    Returns:
        List[str]: A list of strings representing the content of each element.
    
    Example:
        For XML like:
        <scratchpad>
        <quote>First quote text</quote>
        <quote>Second quote text</quote>
        </scratchpad>
        
        parse_list_of_elements(xml_string, "scratchpad", "quote") 
        would return ["First quote text", "Second quote text"]
    """
    object_content: str = get_xml_tag_content(xml_string, object_tag)
    
    # If object tag wasn't found, try searching in the entire string
    if not object_content:
        object_content = xml_string
    
    element_matches = re.findall(rf"<{element_tag}>(.*?)</{element_tag}>", object_content, re.DOTALL)
    elements: List[str] = [element.strip() for element in element_matches]
    return elements


def parse_boolean_tag(xml_string: str, tag_name: str) -> bool:
    """
    Parses a boolean value from an XML tag.
    
    Args:
        xml_string (str): The input XML-like string.
        tag_name (str): The name of the tag containing the boolean value.
    
    Returns:
        bool: True if the tag content is "yes", "true", or "1" (case-insensitive), False otherwise.
    """
    tag_content = get_xml_tag_content(xml_string, tag_name).lower().strip()
    return tag_content in ("yes", "true", "1")


def parse_numeric_tag(xml_string: str, tag_name: str, default: float = 0.0) -> float:
    """
    Parses a numeric value from an XML tag.
    
    Args:
        xml_string (str): The input XML-like string.
        tag_name (str): The name of the tag containing the numeric value.
        default (float): Default value to return if parsing fails.
    
    Returns:
        float: The parsed numeric value, or default if parsing fails.
    """
    tag_content = get_xml_tag_content(xml_string, tag_name).strip()
    try:
        return float(tag_content) if tag_content else default
    except ValueError:
        return default


def validate_expected_tags(xml_string: str, expected_tags: List[str]) -> Dict[str, bool]:
    """
    Validates that expected XML tags are present in the response.
    
    Args:
        xml_string (str): The XML string to validate.
        expected_tags (List[str]): List of tag names that should be present.
    
    Returns:
        Dict[str, bool]: Dictionary mapping tag names to whether they were found.
    """
    validation_results = {}
    for tag in expected_tags:
        tag_content = get_xml_tag_content(xml_string, tag)
        validation_results[tag] = bool(tag_content.strip())
    
    return validation_results
