def generate_modality_analysis(planets):
    """
    Analyze the modality distribution in a birth chart.
    
    Args:
        planets: List of planet objects with sign information
        
    Returns:
        Dictionary with modality analysis data
    """
    # Initialize modality counters
    modalities = {
        "cardinal": 0,
        "fixed": 0,
        "mutable": 0
    }
    
    # Map signs to modalities
    sign_to_modality = {
        "Aries": "cardinal", "Cancer": "cardinal", "Libra": "cardinal", "Capricorn": "cardinal",
        "Taurus": "fixed", "Leo": "fixed", "Scorpio": "fixed", "Aquarius": "fixed",
        "Gemini": "mutable", "Virgo": "mutable", "Sagittarius": "mutable", "Pisces": "mutable"
    }
    
    # Planet importance weights
    planet_weights = {
        "Sun": 3, "Moon": 2.5, 
        "Mercury": 1, "Venus": 1, "Mars": 1,
        "Jupiter": 1, "Saturn": 1,
        "Uranus": 0.5, "Neptune": 0.5, "Pluto": 0.5
    }
    
    # Count each modality with weighting
    total_weight = 0
    planet_details = []
    
    for planet in planets:
        # Handle both name formats (some APIs use 'name', others use 'planet')
        planet_name = planet.get("name", planet.get("planet", ""))
        
        # Handle both sign formats (some use direct sign name, others use object)
        sign_name = None
        if isinstance(planet.get("sign"), dict):
            sign_name = planet.get("sign", {}).get("name", "")
        else:
            sign_name = planet.get("sign", "")
        
        # Skip if not a main celestial body or sign info is missing
        if not planet_name or not sign_name or planet_name in ["North Node", "South Node"]:
            continue
            
        # Get modality for this sign
        modality = sign_to_modality.get(sign_name)
        if not modality:
            continue
            
        # Get weight for this planet
        weight = planet_weights.get(planet_name, 0.5)
        total_weight += weight
        
        # Add to modality count
        modalities[modality] += weight
        
        # Add to planet details
        planet_details.append({
            "planet": planet_name,
            "sign": sign_name,
            "modality": modality,
            "weight": weight
        })
    
    # Calculate percentages
    percentages = {}
    if total_weight > 0:
        for modality, count in modalities.items():
            percentages[modality] = round((count / total_weight) * 100)
    
    # Determine dominant modality
    dominant_modality = max(modalities.items(), key=lambda x: x[1])[0]
    
    # Generate descriptions based on modality distribution
    description = generate_modality_description(dominant_modality, percentages)
    
    # Return the complete analysis
    return {
        "counts": modalities,
        "percentages": percentages,
        "dominant_modality": dominant_modality,
        "planet_details": planet_details,
        "description": description
    }
    
def generate_modality_description(dominant, percentages):
    """Generate a description based on modality distribution."""
    description = {
        "dominant": f"Your dominant modality is {dominant}.",
        "cardinal": get_cardinal_description(percentages["cardinal"]),
        "fixed": get_fixed_description(percentages["fixed"]),
        "mutable": get_mutable_description(percentages["mutable"]),
        "overall": get_overall_modality_description(percentages)
    }
    
    return description
    
def get_cardinal_description(percentage):
    """Get description for cardinal modality based on percentage."""
    if percentage >= 40:
        return "You have a strong cardinal presence, making you initiative-taking, proactive, and driven to start new endeavors."
    elif percentage >= 25:
        return "You have a balanced cardinal energy, providing healthy initiative and leadership when needed."
    else:
        return "You have less cardinal energy, which may manifest as challenges with taking initiative or leadership roles."
        
def get_fixed_description(percentage):
    """Get description for fixed modality based on percentage."""
    if percentage >= 40:
        return "You have a strong fixed presence, giving you determination, loyalty, and steadfastness in your pursuits."
    elif percentage >= 25:
        return "You have a balanced fixed energy, providing stability and persistence when needed."
    else:
        return "You have less fixed energy, which may manifest as challenges with maintaining consistency or seeing things through to completion."
        
def get_mutable_description(percentage):
    """Get description for mutable modality based on percentage."""
    if percentage >= 40:
        return "You have a strong mutable presence, making you adaptable, flexible, and responsive to changing circumstances."
    elif percentage >= 25:
        return "You have a balanced mutable energy, providing adaptability and versatility when needed."
    else:
        return "You have less mutable energy, which may manifest as challenges with flexibility or adapting to change."
        
def get_overall_modality_description(percentages):
    """Get overall modality distribution description."""
    # Check for strong imbalances
    max_modality = max(percentages.items(), key=lambda x: x[1])
    min_modality = min(percentages.items(), key=lambda x: x[1])
    
    if max_modality[1] > 50:
        return f"Your chart shows a strong emphasis on the {max_modality[0]} modality, suggesting this is a dominant force in how you approach challenges and changes in life."
    elif max_modality[1] - min_modality[1] > 30:
        return f"There's a significant imbalance between your {max_modality[0]} and {min_modality[0]} modalities, suggesting you may lean heavily toward {max_modality[0]} approaches."
    else:
        return "Your chart shows a relatively balanced distribution of modalities, suggesting versatility in how you initiate, maintain, and adapt to different life situations." 