def analyze_element_relationships(element_percentages):
    """
    Analyze the relationship between the two most dominant elements.
    
    Args:
        element_percentages: Dictionary with element percentages
        
    Returns:
        Dictionary with element relationship data
    """
    # Skip if we don't have enough data
    if not element_percentages or len(element_percentages) < 2:
        return None
    
    # Get the two most dominant elements
    sorted_elements = sorted(element_percentages.items(), key=lambda x: x[1], reverse=True)
    
    # Only process if we have at least two elements
    if len(sorted_elements) < 2:
        return None
        
    primary_element = sorted_elements[0][0]
    secondary_element = sorted_elements[1][0]
    
    # Define the relationship descriptions
    relationships = {
        ("fire", "fire"): "Pure fire energy creates intense passion, enthusiasm, and drive, but can burn out quickly or be overwhelming.",
        ("fire", "earth"): "Fire and earth can create tension, with fire's spontaneity conflicting with earth's caution, but they also provide balance.",
        ("fire", "air"): "Fire and air create a harmonious blend of inspiration and communication, fueling big ideas and enthusiastic expression.",
        ("fire", "water"): "Fire and water can create steam! This combination balances passion with sensitivity, though can create emotional intensity.",
        
        ("earth", "fire"): "Earth provides grounding for fire's energy, creating practical action, but may feel restrictive to fire's spontaneity.",
        ("earth", "earth"): "Double earth energy creates tremendous stability, reliability, and patience, though may resist necessary changes.",
        ("earth", "air"): "Earth and air can create friction, as earth's practicality may feel limiting to air's theoretical approach.",
        ("earth", "water"): "Earth and water create a nurturing combination, providing emotional security and practical support.",
        
        ("air", "fire"): "Air fans fire's flames, creating inspiring ideas and the communication skills to express them.",
        ("air", "earth"): "Air brings ideas while earth provides structure, though earth may find air too theoretical at times.",
        ("air", "air"): "Double air energy creates intellectual brilliance and social versatility, but may lack emotional groundedness.",
        ("air", "water"): "Air and water combine intellect with emotion, creating empathetic communication, though sometimes conflicting approaches.",
        
        ("water", "fire"): "Water can either temper fire's intensity or be evaporated by it, creating an emotionally passionate dynamic.",
        ("water", "earth"): "Water and earth create a fertile combination, nurturing growth through emotional depth and practical stability.",
        ("water", "air"): "Water adds emotional depth to air's intellectual approach, though may struggle with air's detachment.",
        ("water", "water"): "Double water energy creates profound emotional depth and intuition, though may become overwhelming without boundaries."
    }
    
    # Get the description for this combination
    key = (primary_element, secondary_element)
    description = relationships.get(key, "These elements interact in complex ways, both challenging and supporting each other.")
    
    # Calculate the percentage difference
    primary_percent = element_percentages[primary_element]
    secondary_percent = element_percentages[secondary_element]
    difference = primary_percent - secondary_percent
    
    # Determine balance type
    if difference <= 5:
        balance = "equal"
        balance_description = f"Your {primary_element} and {secondary_element} elements are nearly equal in strength, creating a balanced interaction."
    elif difference <= 15:
        balance = "moderate"
        balance_description = f"Your {primary_element} element is moderately stronger than your {secondary_element} element, leading one while being influenced by the other."
    else:
        balance = "dominant"
        balance_description = f"Your {primary_element} element is significantly stronger than your {secondary_element} element, dominating the relationship."
    
    # Return the complete analysis
    return {
        "primary_element": primary_element,
        "secondary_element": secondary_element,
        "primary_percentage": primary_percent,
        "secondary_percentage": secondary_percent,
        "difference": difference,
        "balance": balance,
        "description": description,
        "balance_description": balance_description
    }

def get_all_element_relationships(element_percentages):
    """
    Get all significant element relationships in the chart.
    
    Args:
        element_percentages: Dictionary with element percentages
        
    Returns:
        List of relationship dictionaries in descending order of significance
    """
    # Skip if we don't have enough data
    if not element_percentages or len(element_percentages) < 2:
        return []
    
    # Define the element pairs
    elements = ["fire", "earth", "air", "water"]
    
    # Relationship significance threshold (only include if both elements are at least this percentage)
    threshold = 15
    
    # Generate all possible relationships
    all_relationships = []
    
    for i, elem1 in enumerate(elements):
        for j, elem2 in enumerate(elements[i:], i):  # Only process each pair once
            # Skip same element unless it's very strong
            if elem1 == elem2 and element_percentages[elem1] < 40:
                continue
                
            # Check if both elements are present in significant amounts
            if element_percentages[elem1] >= threshold and element_percentages[elem2] >= threshold:
                # Get the relationship description
                relationship = get_element_pair_description(elem1, elem2, element_percentages)
                
                # Add to results
                if relationship:
                    # Calculate significance based on combined percentage and interaction strength
                    combined_percentage = element_percentages[elem1] + element_percentages[elem2]
                    interaction_strength = get_interaction_strength(elem1, elem2)
                    
                    significance = combined_percentage * interaction_strength
                    relationship["significance"] = significance
                    
                    all_relationships.append(relationship)
    
    # Sort by significance
    all_relationships.sort(key=lambda x: x["significance"], reverse=True)
    
    # Return top relationships
    return all_relationships[:3]  # Limit to top 3 for clarity

def get_element_pair_description(elem1, elem2, percentages):
    """Get description for a pair of elements."""
    # Define the relationship descriptions
    relationships = {
        ("fire", "fire"): {
            "interaction": "reinforcing",
            "harmony": "harmonious",
            "description": "Double fire creates powerful passion and initiative but can lead to burnout."
        },
        ("fire", "earth"): {
            "interaction": "challenging",
            "harmony": "tense",
            "description": "Fire's spontaneity meets earth's caution, creating productive tension."
        },
        ("fire", "air"): {
            "interaction": "enhancing",
            "harmony": "harmonious",
            "description": "Fire and air create brilliant inspiration and creative expression."
        },
        ("fire", "water"): {
            "interaction": "tempering",
            "harmony": "complex",
            "description": "Fire's passion meets water's emotion, creating transformative steam."
        },
        ("earth", "earth"): {
            "interaction": "reinforcing",
            "harmony": "harmonious",
            "description": "Double earth creates exceptional stability and patience but may resist change."
        },
        ("earth", "air"): {
            "interaction": "balancing",
            "harmony": "tense",
            "description": "Earth grounds air's abstract thinking, bringing ideas to practical reality."
        },
        ("earth", "water"): {
            "interaction": "nurturing",
            "harmony": "harmonious",
            "description": "Earth contains water's flow, creating fertile ground for emotional security."
        },
        ("air", "air"): {
            "interaction": "reinforcing",
            "harmony": "harmonious",
            "description": "Double air creates brilliant intellectual and social connections but may lack grounding."
        },
        ("air", "water"): {
            "interaction": "moderating",
            "harmony": "complex",
            "description": "Air's intellect meets water's emotions, creating empathetic communication."
        },
        ("water", "water"): {
            "interaction": "reinforcing",
            "harmony": "harmonious",
            "description": "Double water creates profound emotional depth and intuition but may overwhelm."
        }
    }
    
    # Ensure consistent ordering for lookup
    if elem1 > elem2:
        elem1, elem2 = elem2, elem1
        
    # Get the description
    key = (elem1, elem2)
    relationship_data = relationships.get(key)
    
    if not relationship_data:
        return None
        
    # Calculate strength difference
    strength1 = percentages[elem1]
    strength2 = percentages[elem2]
    difference = abs(strength1 - strength2)
    
    # Determine balance text
    if difference <= 5:
        balance_text = "evenly balanced"
    elif difference <= 15:
        stronger = elem1 if strength1 > strength2 else elem2
        balance_text = f"{stronger} leading"
    else:
        dominant = elem1 if strength1 > strength2 else elem2
        secondary = elem2 if dominant == elem1 else elem1
        balance_text = f"{dominant} dominant over {secondary}"
    
    # Return formatted relationship
    return {
        "element1": elem1,
        "element2": elem2,
        "element1_percentage": strength1,
        "element2_percentage": strength2,
        "interaction": relationship_data["interaction"],
        "harmony": relationship_data["harmony"],
        "description": relationship_data["description"],
        "balance": balance_text
    }

def get_interaction_strength(elem1, elem2):
    """Get the interaction strength multiplier for element pairs."""
    # Interaction strength is higher for complementary or opposing elements
    interaction_strengths = {
        ("fire", "fire"): 0.8,  # Same element (slightly lower to prioritize interactions)
        ("earth", "earth"): 0.8,
        ("air", "air"): 0.8,
        ("water", "water"): 0.8,
        
        ("fire", "air"): 1.2,  # Complementary elements (higher priority)
        ("earth", "water"): 1.2,
        
        ("fire", "water"): 1.1,  # Opposing elements (interesting tension)
        ("earth", "air"): 1.1,
        
        ("fire", "earth"): 1.0,  # Neutral combinations
        ("air", "water"): 1.0,
    }
    
    # Ensure consistent ordering for lookup
    if elem1 > elem2:
        elem1, elem2 = elem2, elem1
        
    # Get the strength multiplier (default to 1.0)
    key = (elem1, elem2)
    return interaction_strengths.get(key, 1.0) 