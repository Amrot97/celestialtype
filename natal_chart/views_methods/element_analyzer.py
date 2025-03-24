def analyze_elements(planets):
    """
    Analyze the elemental distribution in a birth chart.
    
    Args:
        planets: List of planet objects with sign information
        
    Returns:
        Dictionary with element analysis data
    """
    # Initialize element counters
    elements = {
        "fire": 0,
        "earth": 0,
        "air": 0,
        "water": 0
    }
    
    # Map signs to elements
    sign_to_element = {
        "Aries": "fire", "Leo": "fire", "Sagittarius": "fire",
        "Taurus": "earth", "Virgo": "earth", "Capricorn": "earth",
        "Gemini": "air", "Libra": "air", "Aquarius": "air",
        "Cancer": "water", "Scorpio": "water", "Pisces": "water"
    }
    
    # Planet importance weights
    planet_weights = {
        "Sun": 3, "Moon": 2.5, 
        "Mercury": 1, "Venus": 1, "Mars": 1,
        "Jupiter": 1, "Saturn": 1,
        "Uranus": 0.5, "Neptune": 0.5, "Pluto": 0.5
    }
    
    # Count each element with weighting
    total_weight = 0
    planet_details = []
    
    for planet in planets:
        planet_name = planet.get("name", "")
        sign_name = planet.get("sign", "")
        
        # Skip if not a main celestial body or sign info is missing
        if not planet_name or not sign_name or planet_name in ["North Node", "South Node"]:
            continue
            
        # Get element for this sign
        element = sign_to_element.get(sign_name)
        if not element:
            continue
            
        # Get weight for this planet
        weight = planet_weights.get(planet_name, 0.5)
        total_weight += weight
        
        # Add to element count
        elements[element] += weight
        
        # Add to planet details
        planet_details.append({
            "planet": planet_name,
            "sign": sign_name,
            "element": element,
            "weight": weight
        })
    
    # Calculate percentages
    percentages = {}
    if total_weight > 0:
        for element, count in elements.items():
            percentages[element] = round((count / total_weight) * 100)
    
    # Determine dominant element
    dominant_element = max(elements.items(), key=lambda x: x[1])[0]
    
    # Determine weakest element
    weakest_element = min(elements.items(), key=lambda x: x[1])[0]
    
    # Generate element balance assessment
    element_balance = {}
    
    # Fire-Earth axis
    fire_earth_balance = elements["fire"] - elements["earth"]
    if fire_earth_balance > 2:
        element_balance["fire_earth"] = "Strong fire emphasis over earth"
    elif fire_earth_balance < -2:
        element_balance["fire_earth"] = "Strong earth emphasis over fire"
    else:
        element_balance["fire_earth"] = "Balanced fire and earth"
        
    # Air-Water axis
    air_water_balance = elements["air"] - elements["water"]
    if air_water_balance > 2:
        element_balance["air_water"] = "Strong air emphasis over water"
    elif air_water_balance < -2:
        element_balance["air_water"] = "Strong water emphasis over air"
    else:
        element_balance["air_water"] = "Balanced air and water"
    
    # Generate descriptions based on element distribution
    description = generate_element_description(dominant_element, weakest_element, percentages)
    
    # Return the complete analysis
    return {
        "counts": elements,
        "percentages": percentages,
        "dominant_element": dominant_element,
        "weakest_element": weakest_element,
        "element_balance": element_balance,
        "planet_details": planet_details,
        "description": description
    }
    
def generate_element_description(dominant, weakest, percentages):
    """Generate a description based on element distribution."""
    description = {
        "dominant": f"Your dominant element is {dominant.capitalize()}.",
        "weakest": f"Your least expressed element is {weakest.capitalize()}.",
        "fire": get_fire_description(percentages["fire"]),
        "earth": get_earth_description(percentages["earth"]),
        "air": get_air_description(percentages["air"]),
        "water": get_water_description(percentages["water"]),
        "overall": get_overall_element_description(percentages)
    }
    
    return description
    
def get_fire_description(percentage):
    """Get description for fire element based on percentage."""
    if percentage >= 40:
        return "You have a strong fire element, giving you enthusiasm, courage, and a pioneering spirit."
    elif percentage >= 25:
        return "You have a balanced fire element, providing healthy levels of motivation and self-expression."
    else:
        return "You have less fire energy, which may manifest as challenges with motivation or assertiveness."
        
def get_earth_description(percentage):
    """Get description for earth element based on percentage."""
    if percentage >= 40:
        return "You have a strong earth element, making you practical, reliable, and grounded."
    elif percentage >= 25:
        return "You have a balanced earth element, providing stability and practicality when needed."
    else:
        return "You have less earth energy, which may manifest as challenges with routine or material concerns."
        
def get_air_description(percentage):
    """Get description for air element based on percentage."""
    if percentage >= 40:
        return "You have a strong air element, giving you intellectual clarity, social skills, and adaptability."
    elif percentage >= 25:
        return "You have a balanced air element, providing good communication and intellectual abilities."
    else:
        return "You have less air energy, which may manifest as challenges with detachment or abstract thinking."
        
def get_water_description(percentage):
    """Get description for water element based on percentage."""
    if percentage >= 40:
        return "You have a strong water element, giving you emotional depth, intuition, and empathy."
    elif percentage >= 25:
        return "You have a balanced water element, providing emotional awareness and compassion."
    else:
        return "You have less water energy, which may manifest as challenges with emotional expression or intuition."
        
def get_overall_element_description(percentages):
    """Get overall element distribution description."""
    # Check for strong imbalances
    max_element = max(percentages.items(), key=lambda x: x[1])
    min_element = min(percentages.items(), key=lambda x: x[1])
    
    if max_element[1] > 50:
        return f"Your chart shows a strong emphasis on the {max_element[0]} element, suggesting this is a dominant force in your personality and approach to life."
    elif max_element[1] - min_element[1] > 30:
        return f"There's a significant imbalance between your {max_element[0]} and {min_element[0]} elements, suggesting potential challenges in integrating these energies."
    else:
        return "Your chart shows a relatively balanced distribution of elements, suggesting versatility in how you approach different life situations." 