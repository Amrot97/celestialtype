"""
Module for generating the Overview tab data structure for the CelestialType API.
This module extracts and formats data from various parts of the API response
to create a consolidated overview of the natal chart.
"""

def generate_overview_tab(user_name, date_of_birth, place_of_birth, coordinates, 
                         psychological_insights, stellium_descriptions, 
                         modality_analysis, elements_tab):
    """
    Generate the overview tab data structure from existing API data.
    
    Args:
        user_name (str): User's name
        date_of_birth (str): Date of birth in YYYY-MM-DD format
        place_of_birth (str): Place of birth name
        coordinates (dict): Latitude and longitude coordinates
        psychological_insights (list): Array of planet insights
        stellium_descriptions (list): Array of stellium descriptions
        modality_analysis (dict): Modality analysis data
        elements_tab (dict): Elements tab data
        
    Returns:
        dict: Complete overview tab structure
    """
    # 1. Extract basic info
    basic_info = {
        "name": user_name,
        "sun_sign": extract_sun_sign(psychological_insights),
        "date_of_birth": date_of_birth,
        "place_of_birth": {
            "name": place_of_birth,
            "coordinates": coordinates
        }
    }
    
    # 2. Build cosmic profile
    dominant_elements = elements_tab.get("distribution", {}).get("dominant_elements", [])
    elemental_description = generate_elements_description(dominant_elements, elements_tab)
    
    # Format element balance as array of objects
    element_balance = []
    for element in ["Fire", "Earth", "Air", "Water"]:
        element_balance.append({
            "name": element,
            "value": elements_tab.get("distribution", {}).get(element, 0)
        })
    
    # Format modality balance as array of objects
    modality_balance = []
    for modality in ["cardinal", "fixed", "mutable"]:
        modality_balance.append({
            "name": modality.capitalize(),
            "value": modality_analysis.get("percentages", {}).get(modality, 0)
        })
    
    cosmic_profile = {
        "elemental_balance": {
            "distribution": element_balance,
            "dominant_elements": dominant_elements,
            "description": elemental_description
        },
        "modality_balance": modality_balance,
        "dominant_planets": calculate_dominant_planets(psychological_insights)
    }
    
    # 3. Extract key insights
    key_insights = {
        "sun": extract_planet_insight(psychological_insights, "Sun", "Core Identity"),
        "moon": extract_planet_insight(psychological_insights, "Moon", "Emotions"),
        "venus": extract_planet_insight(psychological_insights, "Venus", "Values & Love"),
        "mars": extract_planet_insight(psychological_insights, "Mars", "Action & Drive")
    }
    
    # 4. Format stellium info if present
    stellium = format_stellium_for_overview(stellium_descriptions)
    
    # 5. Return complete overview structure
    return {
        "basic_info": basic_info,
        "cosmic_profile": cosmic_profile,
        "key_insights": key_insights,
        "stellium": stellium
    }

def extract_sun_sign(psychological_insights):
    """
    Extract sun sign from psychological insights.
    
    Args:
        psychological_insights (list): Array of planet insights
        
    Returns:
        str: Sun sign name or "Unknown" if not found
    """
    for insight in psychological_insights:
        if insight.get("title", "").startswith("Sun in "):
            return insight["title"].replace("Sun in ", "")
    return "Unknown"

def generate_elements_description(dominant_elements, elements_tab):
    """
    Generate a user-friendly description of the elemental balance.
    
    Args:
        dominant_elements (list): List of dominant elements
        elements_tab (dict): Complete elements tab data
        
    Returns:
        str: Formatted description of the elemental balance
    """
    if not dominant_elements:
        return "Your chart shows a relatively balanced distribution of elements."
    
    # Use the distribution description if available
    if elements_tab.get("distribution", {}).get("description"):
        return elements_tab["distribution"]["description"]
    
    # Or build a custom description based on dominant elements
    if len(dominant_elements) == 1:
        elem = dominant_elements[0].capitalize()
        return f"Your {elem} emphasis gives you {get_element_qualities(elem.lower())}. This elemental influence shapes how you approach challenges and opportunities in your life."
    
    elif len(dominant_elements) >= 2:
        elem1 = dominant_elements[0].capitalize()
        elem2 = dominant_elements[1].capitalize()
        return f"Your {elem1}-{elem2} combination blends {get_element_qualities(elem1.lower())} with {get_element_qualities(elem2.lower())}. This creates a dynamic approach that allows you to draw on different strengths in various situations."
    
    return "Your chart shows a relatively balanced distribution of elements."

def get_element_qualities(element):
    """
    Get brief quality descriptions for elements.
    
    Args:
        element (str): Element name (fire, earth, air, water)
        
    Returns:
        str: Quality description
    """
    qualities = {
        "fire": "enthusiasm, inspiration, and courage",
        "earth": "practicality, reliability, and groundedness",
        "air": "intellectual clarity, communication skills, and adaptability",
        "water": "emotional depth, intuition, and empathy"
    }
    return qualities.get(element, "")

def generate_modality_description(modality_analysis):
    """
    Generate a user-friendly description of the modality balance.
    
    Args:
        modality_analysis (dict): Modality analysis data
        
    Returns:
        str: Formatted description
    """
    # Use the overall description if available
    if modality_analysis.get("description", {}).get("overall"):
        return modality_analysis["description"]["overall"]
    
    # Or the dominant modality description
    dom_modality = modality_analysis.get("dominant_modality", "").capitalize()
    if dom_modality and modality_analysis.get("description", {}).get(dom_modality.lower()):
        return f"Your dominant {dom_modality} modality {modality_analysis['description'][dom_modality.lower()]}"
    
    # Or a default description
    return "Your chart shows a balance of Cardinal, Fixed, and Mutable modalities, giving you versatility in how you approach situations."

def extract_planet_insight(psychological_insights, planet_name, title):
    """
    Extract insight for a specific planet and format it for overview.
    
    Args:
        psychological_insights (list): Array of planet insights
        planet_name (str): Name of the planet (Sun, Moon, etc.)
        title (str): Title for this insight section
        
    Returns:
        dict: Formatted planet insight
    """
    for insight in psychological_insights:
        if insight.get("title", "").startswith(f"{planet_name} in "):
            sign = insight["title"].replace(f"{planet_name} in ", "")
            
            # Get the description based on planet type
            description = ""
            if planet_name == "Sun":
                description = insight.get("explanation", "")
            elif planet_name == "Moon":
                description = insight.get("explanation", "")
            elif planet_name == "Venus":
                description = insight.get("strengths_in_connection", "")
            elif planet_name == "Mars":
                description = insight.get("strengths_in_action", "")
            
            return {
                "sign": sign,
                "title": title,
                "description": description
            }
    
    # Default if not found
    return {
        "sign": "Unknown",
        "title": title,
        "description": "Data not available"
    }

def calculate_dominant_planets(psychological_insights):
    """
    Calculate dominant planets based on psychological insights.
    
    This is a simplified implementation that selects key planets based on
    typical astrological importance. A more sophisticated algorithm would
    consider angular position, essential dignities, etc.
    
    Args:
        psychological_insights (list): Array of planet insights
        
    Returns:
        list: Array of objects with planet name and percentage value
    """
    # Extract all planetary positions
    planets = []
    for insight in psychological_insights:
        title = insight.get("title", "")
        for planet in ["Sun", "Moon", "Mercury", "Venus", "Mars", "Jupiter", "Saturn"]:
            if title.startswith(f"{planet} in "):
                planets.append(planet)
    
    # Define planet weights for importance calculation
    planet_weights = {
        "Sun": 30,
        "Moon": 25,
        "Mercury": 10, 
        "Venus": 10,
        "Mars": 10,
        "Jupiter": 8,
        "Saturn": 7,
        "Uranus": 0,  # Not including outer planets in dominant calculation
        "Neptune": 0,
        "Pluto": 0
    }
    
    # Calculate weighted scores for each planet
    planet_scores = {}
    total_score = 0
    
    for planet in planets:
        weight = planet_weights.get(planet, 0)
        planet_scores[planet] = weight
        total_score += weight
    
    # Calculate percentages
    planet_percentages = {}
    for planet, score in planet_scores.items():
        percentage = int(round((score / total_score) * 100)) if total_score > 0 else 0
        planet_percentages[planet] = percentage
    
    # Select top 3 planets based on score and format as array of objects
    sorted_planets = sorted(planet_percentages.items(), key=lambda x: x[1], reverse=True)
    result = []
    
    # Take top 3 planets and format as objects
    for planet, percentage in sorted_planets[:3]:
        result.append({
            "name": planet,
            "value": percentage
        })
    
    return result

def format_stellium_for_overview(stellium_descriptions):
    """
    Format stellium descriptions for the overview section.
    
    Args:
        stellium_descriptions (list): Array of stellium descriptions
        
    Returns:
        dict: Formatted stellium information
    """
    if not stellium_descriptions:
        return {
            "has_stellium": False
        }
    
    # Use the first stellium if multiple exist
    stellium = stellium_descriptions[0]
    
    return {
        "has_stellium": True,
        "title": stellium.get("title", ""),
        "subtitle": stellium.get("subtitle", ""),
        "description": stellium.get("text", "")
    } 