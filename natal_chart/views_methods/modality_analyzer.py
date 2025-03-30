from natal_chart.views_methods.planet_descriptions.modality_descriptions import MODALITY_DESCRIPTIONS, OVERALL_PATTERN_TEMPLATES

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
    description = generate_modality_description(dominant_modality, percentages, modalities)
    
    # Return only the dominant modality and description in the analysis
    return {
        "dominant_modality": dominant_modality,
        "description": description
    }
    
def generate_modality_description(dominant, percentages, counts):
    """Generate a comprehensive description based on modality distribution."""
    # Get detailed descriptions for each modality
    description = {
        "dominant": f"Your dominant modality is {dominant}.",
        "cardinal": get_cardinal_description(percentages["cardinal"]),
        "fixed": get_fixed_description(percentages["fixed"]),
        "mutable": get_mutable_description(percentages["mutable"]),
        "overall": get_overall_modality_description(percentages)
    }
    
    # Add detailed dominant modality information
    dominant_cap = dominant.capitalize()
    if dominant_cap in MODALITY_DESCRIPTIONS:
        dom_desc = MODALITY_DESCRIPTIONS[dominant_cap]
        
        # Determine if it's high or low expression
        level = "high" if percentages[dominant] >= 40 else "low"
        
        # Add detailed descriptions
        description["dominant_title"] = dom_desc["title"]
        description["dominant_core_traits"] = dom_desc["core_traits"]
        description["dominant_description"] = dom_desc[f"{level}_description"]
        description["dominant_strengths"] = dom_desc[f"{level}_strengths"]
        description["dominant_challenges"] = dom_desc[f"{level}_challenges"]
        description["dominant_career_insights"] = dom_desc[f"{level}_career_insights"]
        description["dominant_relationship_insights"] = dom_desc[f"{level}_relationship_insights"]
        description["dominant_balance_strategies"] = dom_desc[f"{level}_balance_strategies"]
        description["dominant_examples"] = dom_desc[f"{level}_examples"]
    
    # Add overall pattern description
    pattern_key = get_pattern_key(percentages)
    if pattern_key in OVERALL_PATTERN_TEMPLATES:
        pattern = OVERALL_PATTERN_TEMPLATES[pattern_key]
        
        # Format the percentages and modalities for the template
        modalities_text = ""
        percentages_text = ""
        
        if pattern_key == "multiple_dominant" or pattern_key == "lacking_some":
            # For these patterns, we need to specify which modalities
            sorted_modalities = sorted(percentages.items(), key=lambda x: x[1], reverse=True)
            
            if pattern_key == "multiple_dominant":
                top_modalities = [m[0].capitalize() for m in sorted_modalities[:2]]
                top_percentages = [f"{m[1]}%" for m in sorted_modalities[:2]]
                modalities_text = " and ".join(top_modalities)
                percentages_text = " and ".join(top_percentages)
            else:  # lacking_some
                bottom_modality = sorted_modalities[-1][0].capitalize()
                bottom_percentage = f"{sorted_modalities[-1][1]}%"
                modalities_text = bottom_modality
                percentages_text = bottom_percentage
                
        # Add pattern descriptions
        if pattern_key == "cardinal_dominant" or pattern_key == "fixed_dominant" or pattern_key == "mutable_dominant":
            percentage = percentages[pattern_key.split('_')[0]]
            description["pattern_summary"] = pattern["summary"].format(percentage=percentage)
        else:
            description["pattern_summary"] = pattern["summary"].format(modalities=modalities_text, percentages=percentages_text)
            
        description["pattern_life_approach"] = pattern["life_approach"]
        description["pattern_practical_advice"] = pattern["practical_advice"].format(modalities=modalities_text)
    
    return description
    
def get_cardinal_description(percentage):
    """Get detailed description for cardinal modality based on percentage."""
    if percentage >= 40:
        return "You have a strong cardinal presence, making you initiative-taking, proactive, and driven to start new endeavors. " + \
               MODALITY_DESCRIPTIONS["Cardinal"]["high_description"]
    elif percentage >= 25:
        return "You have a balanced cardinal energy, providing healthy initiative and leadership when needed."
    else:
        return "You have less cardinal energy, which may manifest as challenges with taking initiative or leadership roles. " + \
               MODALITY_DESCRIPTIONS["Cardinal"]["low_description"]
        
def get_fixed_description(percentage):
    """Get detailed description for fixed modality based on percentage."""
    if percentage >= 40:
        return "You have a strong fixed presence, giving you determination, loyalty, and steadfastness in your pursuits. " + \
               MODALITY_DESCRIPTIONS["Fixed"]["high_description"]
    elif percentage >= 25:
        return "You have a balanced fixed energy, providing stability and persistence when needed."
    else:
        return "You have less fixed energy, which may manifest as challenges with maintaining consistency or seeing things through to completion. " + \
               MODALITY_DESCRIPTIONS["Fixed"]["low_description"]
        
def get_mutable_description(percentage):
    """Get detailed description for mutable modality based on percentage."""
    if percentage >= 40:
        return "You have a strong mutable presence, making you adaptable, flexible, and responsive to changing circumstances. " + \
               MODALITY_DESCRIPTIONS["Mutable"]["high_description"]
    elif percentage >= 25:
        return "You have a balanced mutable energy, providing adaptability and versatility when needed."
    else:
        return "You have less mutable energy, which may manifest as challenges with flexibility or adapting to change. " + \
               MODALITY_DESCRIPTIONS["Mutable"]["low_description"]
        
def get_overall_modality_description(percentages):
    """Get overall modality distribution description."""
    pattern_key = get_pattern_key(percentages)
    
    # Use pattern templates for the overall description
    if pattern_key in OVERALL_PATTERN_TEMPLATES:
        pattern = OVERALL_PATTERN_TEMPLATES[pattern_key]
        
        # Basic descriptions based on pattern
        if pattern_key == "cardinal_dominant":
            percentage = percentages["cardinal"]
            return pattern["summary"].format(percentage=percentage)
        elif pattern_key == "fixed_dominant":
            percentage = percentages["fixed"]
            return pattern["summary"].format(percentage=percentage)
        elif pattern_key == "mutable_dominant":
            percentage = percentages["mutable"]
            return pattern["summary"].format(percentage=percentage)
        elif pattern_key == "balanced":
            return pattern["summary"]
        else:
            # For multiple_dominant or lacking_some, we need to format the text
            sorted_modalities = sorted(percentages.items(), key=lambda x: x[1], reverse=True)
            
            if pattern_key == "multiple_dominant":
                top_modalities = [m[0].capitalize() for m in sorted_modalities[:2]]
                top_percentages = [f"{m[1]}%" for m in sorted_modalities[:2]]
                modalities_text = " and ".join(top_modalities)
                percentages_text = " and ".join(top_percentages)
                return pattern["summary"].format(modalities=modalities_text, percentages=percentages_text)
            else:  # lacking_some
                bottom_modality = sorted_modalities[-1][0].capitalize()
                bottom_percentage = f"{sorted_modalities[-1][1]}%"
                return pattern["summary"].format(modalities=bottom_modality, percentages=bottom_percentage)
    
    # Fallback for any other case
    return "Your chart shows a unique distribution of modalities, suggesting a personalized approach to initiating, maintaining, and adapting to life's challenges."

def get_pattern_key(percentages):
    """Determine which pattern template to use based on the percentages."""
    sorted_modalities = sorted(percentages.items(), key=lambda x: x[1], reverse=True)
    
    # Check for dominant modality (over 50%)
    if sorted_modalities[0][1] > 50:
        return f"{sorted_modalities[0][0]}_dominant"
    
    # Check for highly balanced (all within 10% of each other)
    if abs(sorted_modalities[0][1] - sorted_modalities[2][1]) <= 10:
        return "balanced"
    
    # Check for two similarly strong modalities
    if abs(sorted_modalities[0][1] - sorted_modalities[1][1]) <= 10 and \
       sorted_modalities[0][1] - sorted_modalities[2][1] > 15:
        return "multiple_dominant"
    
    # Otherwise, it's a case of having less of some modality
    return "lacking_some" 