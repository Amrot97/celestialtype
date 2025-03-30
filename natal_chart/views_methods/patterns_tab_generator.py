"""
Module for generating the Patterns tab data structure for the CelestialType API.
This module combines stellium descriptions and modality analysis to create a
consolidated view of the notable patterns in the natal chart.
"""

def generate_patterns_tab(stellium_descriptions, modality_analysis):
    """
    Generate the patterns tab data structure from stellium and modality data.
    
    Args:
        stellium_descriptions (list): Array of stellium descriptions
        modality_analysis (dict): Modality analysis data
        
    Returns:
        dict: Complete patterns tab structure
    """
    # 1. Format modality section
    modality_section = format_modality_section(modality_analysis)
    
    # 2. Format stellium section
    stellium_section = format_stellium_section(stellium_descriptions)
    
    # 3. Return complete patterns tab structure
    return {
        "modality": modality_section,
        "stellium": stellium_section
    }

def format_modality_section(modality_analysis):
    """
    Format modality analysis data for the patterns tab.
    
    Args:
        modality_analysis (dict): Modality analysis data
        
    Returns:
        dict: Formatted modality section
    """
    if not modality_analysis:
        return {
            "has_dominant_modality": False
        }
    
    dominant_modality = modality_analysis.get("dominant_modality", "").capitalize()
    
    # Get detailed descriptions
    description = modality_analysis.get("description", {})
    
    # Get core_traits from MODALITY_DESCRIPTIONS if available
    from natal_chart.views_methods.planet_descriptions.modality_descriptions import MODALITY_DESCRIPTIONS
    core_traits = ""
    if dominant_modality in MODALITY_DESCRIPTIONS:
        core_traits = MODALITY_DESCRIPTIONS[dominant_modality].get("core_traits", "")
    
    # Format key information about the dominant modality
    return {
        "has_dominant_modality": True,
        "dominant_modality": dominant_modality,
        "core_traits": core_traits,
        "distribution": modality_analysis.get("modality_percentages", []),
        "title": description.get("dominant_title", f"{dominant_modality} Energy"),
        "summary": description.get("pattern_summary", description.get("overall", "")),
        "detailed_description": description.get("dominant_description", ""),
        "strengths": description.get("dominant_strengths", []),
        "challenges": description.get("dominant_challenges", []),
        "practical_advice": description.get("pattern_practical_advice", ""),
        "life_approach": description.get("pattern_life_approach", ""),
        "career_insights": description.get("dominant_career_insights", ""),
        "relationship_insights": description.get("dominant_relationship_insights", ""),
        "balance_strategies": description.get("dominant_balance_strategies", []),
    }

def format_stellium_section(stellium_descriptions):
    """
    Format stellium descriptions for the patterns tab.
    
    Args:
        stellium_descriptions (list): Array of stellium descriptions
        
    Returns:
        dict: Formatted stellium section
    """
    if not stellium_descriptions:
        return {
            "has_stellium": False
        }
    
    # Create array of stellium information
    stelliums = []
    for stellium in stellium_descriptions:
        stelliums.append({
            "planets": stellium.get("planets", []),
            "title": stellium.get("title", ""),
            "subtitle": stellium.get("subtitle", ""),
            "description": stellium.get("text", "")
        })
    
    return {
        "has_stellium": True,
        "count": len(stelliums),
        "stelliums": stelliums
    } 