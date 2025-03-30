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
    
    # Format element percentages as array of objects for consistent API structure
    element_percentages = []
    for element, value in percentages.items():
        element_percentages.append({
            "name": element.capitalize(),
            "value": value
        })
    
    # Sort by value in descending order for better presentation
    element_percentages = sorted(element_percentages, key=lambda x: x["value"], reverse=True)
    
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
    
    # Return the analysis without planet_details
    return {
        "counts": elements,
        "percentages": percentages,
        "element_percentages": element_percentages,
        "dominant_element": dominant_element,
        "weakest_element": weakest_element,
        "element_balance": element_balance,
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

# New functions to support Elements Tab UI structure

def calculate_element_percentages(planet_list):
    """
    Calculate element percentages for a list of planets.
    
    Args:
        planet_list: List of planet objects
        
    Returns:
        Dictionary with element percentages
    """
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
    
    # Initialize element counters
    elements = {
        "fire": 0,
        "earth": 0,
        "air": 0,
        "water": 0
    }
    
    # Count each element with weighting
    total_weight = 0
    
    for planet in planet_list:
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
    
    # Calculate percentages
    percentages = {}
    if total_weight > 0:
        for element, count in elements.items():
            percentages[element] = round((count / total_weight) * 100)
    else:
        # Default equal distribution if no planets
        percentages = {
            "fire": 25,
            "earth": 25,
            "air": 25,
            "water": 25
        }
    
    return percentages

def separate_conscious_unconscious_elements(planets):
    """
    Separate planets into personal (conscious) and transpersonal (unconscious) groups
    and analyze their elemental distribution.
    
    Args:
        planets: List of planet objects
        
    Returns:
        Dictionary with personal and transpersonal planet element analysis
    """
    # Define personal and transpersonal planets
    personal_planets = ["Sun", "Moon", "Mercury", "Venus", "Mars"]
    transpersonal_planets = ["Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
    
    # Filter planets into groups
    personal = [p for p in planets if p.get('name') in personal_planets]
    transpersonal = [p for p in planets if p.get('name') in transpersonal_planets]
    
    # Analyze each group separately
    personal_analysis = calculate_element_percentages(personal)
    transpersonal_analysis = calculate_element_percentages(transpersonal)
    
    # Generate interpretation based on differences
    interpretation = generate_conscious_unconscious_interpretation(
        personal_analysis, 
        transpersonal_analysis
    )
    
    # Convert to name/value pair format
    personal_formatted = []
    transpersonal_formatted = []
    
    for element in ["fire", "earth", "air", "water"]:
        personal_formatted.append({
            "name": element.capitalize(),
            "value": personal_analysis[element]
        })
        transpersonal_formatted.append({
            "name": element.capitalize(),
            "value": transpersonal_analysis[element]
        })
    
    return {
        "personal_planets": personal_formatted,
        "transpersonal_planets": transpersonal_formatted,
        "interpretation": interpretation
    }

def generate_conscious_unconscious_interpretation(personal, transpersonal):
    """
    Generate interpretation text comparing conscious and unconscious elements.
    
    Args:
        personal: Dictionary with personal planet element percentages
        transpersonal: Dictionary with transpersonal planet element percentages
        
    Returns:
        String with interpretation
    """
    # Identify dominant elements in each
    dominant_personal = max(personal.items(), key=lambda x: x[1])[0]
    dominant_transpersonal = max(transpersonal.items(), key=lambda x: x[1])[0]
    
    # Find secondary elements
    personal_items = sorted(personal.items(), key=lambda x: x[1], reverse=True)
    transpersonal_items = sorted(transpersonal.items(), key=lambda x: x[1], reverse=True)
    
    secondary_personal = personal_items[1][0] if len(personal_items) > 1 else None
    secondary_transpersonal = transpersonal_items[1][0] if len(transpersonal_items) > 1 else None
    
    # Check for alignment or disconnect
    if dominant_personal == dominant_transpersonal:
        return f"You consciously identify with {dominant_personal} qualities (enthusiasm, self-expression) and these also dominate your unconscious patterns. This suggests alignment between your conscious self-image and deeper psychological patterns."
    else:
        return f"You consciously identify with {dominant_personal} qualities ({get_element_qualities(dominant_personal)}) and express them readily in your daily life. However, your unconscious patterns are dominated by {dominant_transpersonal} ({get_element_qualities(dominant_transpersonal)}). This suggests a disconnect between your conscious self-image and deeper psychological patterns."

def get_element_qualities(element):
    """Get brief quality descriptions for elements."""
    qualities = {
        "fire": "enthusiasm, creativity",
        "earth": "practicality, stability",
        "air": "intellect, communication",
        "water": "emotion, intuition"
    }
    return qualities.get(element, "")

def get_element_balance_title(percentages):
    """
    Generate a title for the element balance section.
    
    Args:
        percentages: Dictionary with element percentages
        
    Returns:
        String with title
    """
    # Sort elements by percentage
    sorted_elements = sorted(percentages.items(), key=lambda x: x[1], reverse=True)
    
    # Get top two elements if they're significant
    dominant = sorted_elements[0][0].capitalize()
    
    # Check if there's a clear secondary element
    if len(sorted_elements) > 1 and sorted_elements[1][1] >= 25:
        secondary = sorted_elements[1][0].capitalize()
        return f"Your Element Balance: {dominant}-{secondary} Emphasis"
    else:
        return f"Your Element Balance: {dominant} Emphasis"

def format_relationship_data(relationship_data):
    """
    Format element relationship data for UI presentation.
    
    Args:
        relationship_data: Raw relationship data from analyze_element_relationships
        
    Returns:
        Formatted relationship data matching UI structure
    """
    if not relationship_data:
        return {
            "primary_relationship": "balanced",
            "title": "Element Relationship: Balanced",
            "subtitle": "Balanced Elemental Expression",
            "description": "Your chart shows a relatively balanced distribution of elements, allowing you to access different elemental qualities as needed.",
            "strengths": [
                "Adaptability across different situations",
                "Versatile problem-solving approaches",
                "Balanced perspective on challenges",
                "Ability to relate to different types of people",
                "Flexible response to changing circumstances"
            ],
            "integration_strategies": [
                "Recognize which element is most appropriate for different situations",
                "Notice when you might need to emphasize a particular element",
                "Develop awareness of which elemental energy you're expressing",
                "Practice consciously shifting between different elemental approaches",
                "Appreciate your natural versatility"
            ]
        }
    
    # Get primary relationship key
    primary = relationship_data.get('primary_element', '').capitalize()
    secondary = relationship_data.get('secondary_element', '').capitalize()
    
    # Get relationship title
    relationship_title = f"Element Relationship: {primary}-{secondary}"
    
    # Get relationship subtitle
    if primary == "Fire" and secondary == "Earth":
        subtitle = "Fire-Earth Relationship: Manifesting Vision"
    elif primary == "Fire" and secondary == "Air":
        subtitle = "Fire-Air Relationship: Inspired Communication"
    elif primary == "Fire" and secondary == "Water":
        subtitle = "Fire-Water Relationship: Passionate Depth"
    elif primary == "Earth" and secondary == "Fire":
        subtitle = "Earth-Fire Relationship: Practical Creativity"
    elif primary == "Earth" and secondary == "Air":
        subtitle = "Earth-Air Relationship: Practical Innovation"
    elif primary == "Earth" and secondary == "Water":
        subtitle = "Earth-Water Relationship: Nurturing Foundation"
    elif primary == "Air" and secondary == "Fire":
        subtitle = "Air-Fire Relationship: Dynamic Ideas"
    elif primary == "Air" and secondary == "Earth":
        subtitle = "Air-Earth Relationship: Grounded Thinking"
    elif primary == "Air" and secondary == "Water":
        subtitle = "Air-Water Relationship: Emotional Intelligence"
    elif primary == "Water" and secondary == "Fire":
        subtitle = "Water-Fire Relationship: Emotional Passion"
    elif primary == "Water" and secondary == "Earth":
        subtitle = "Water-Earth Relationship: Emotional Stability"
    elif primary == "Water" and secondary == "Air":
        subtitle = "Water-Air Relationship: Intuitive Communication"
    else:
        subtitle = f"{primary}-{secondary} Relationship"
    
    # Generate strengths and integration strategies
    strengths, integration_strategies = get_relationship_strengths_strategies(primary.lower(), secondary.lower())
    
    # Format for UI
    return {
        "primary_relationship": f"{primary.lower()}-{secondary.lower()}",
        "title": relationship_title,
        "subtitle": subtitle,
        "description": relationship_data.get('description', f"When {primary} and {secondary} combine in your chart, they create a dynamic interplay between different aspects of your personality."),
        "strengths": strengths,
        "integration_strategies": integration_strategies
    }

def get_relationship_strengths_strategies(element1, element2):
    """
    Get strengths and integration strategies for element combinations.
    
    Args:
        element1: First element
        element2: Second element
        
    Returns:
        Tuple of (strengths list, integration strategies list)
    """
    # Common strengths and strategies for all combinations
    default_strengths = [
        "Adaptability across different situations",
        "Balance between different approaches",
        "Versatile skill set",
        "Ability to draw on multiple resources"
    ]
    
    default_strategies = [
        "Notice when to emphasize different elemental qualities",
        "Practice consciously shifting between approaches",
        "Appreciate your natural versatility"
    ]
    
    # Fire-Earth
    if (element1 == "fire" and element2 == "earth") or (element1 == "earth" and element2 == "fire"):
        return [
            "Transform creative ideas into practical reality",
            "Balance vision with methodical implementation",
            "Inspire others while delivering concrete results",
            "Natural talent for entrepreneurship",
            "Sustainable creativity that doesn't burn out quickly"
        ], [
            "Create a two-phase approach: visioning (Fire) then implementation (Earth)",
            "Practice patience with the manifestation process",
            "Use Earth energy to create sustainable structures",
            "Balance spontaneity with planning",
            "Recognize when to shift between inspired action and methodical progress"
        ]
    
    # Fire-Air
    elif (element1 == "fire" and element2 == "air") or (element1 == "air" and element2 == "fire"):
        return [
            "Exceptional ability to communicate ideas with passion",
            "Creative thinking that generates innovative solutions",
            "Natural talent for inspiring others through communication",
            "Dynamic social presence that energizes groups",
            "Ability to turn concepts into exciting initiatives"
        ], [
            "Create systems for capturing ideas while maintaining focus",
            "Balance social engagement with creative time",
            "Use writing or mind-mapping to channel inspiration",
            "Practice focusing on one project at a time",
            "Collaborate with earth-dominant individuals for implementation"
        ]
    
    # Fire-Water
    elif (element1 == "fire" and element2 == "water") or (element1 == "water" and element2 == "fire"):
        return [
            "Emotionally authentic creative expression",
            "Intuitive leadership that inspires while remaining sensitive",
            "Ability to transform emotional experiences into creative inspiration",
            "Passionate empathy that allows deep connection with others",
            "Capacity for both enthusiastic action and emotional reflection"
        ], [
            "Create rituals that honor both expression and emotional reflection",
            "Practice emotional awareness during creative endeavors",
            "Use artistic expression as a bridge between emotion and action",
            "Balance social engagement with time for emotional processing",
            "Develop healthy outlets for intense emotional-creative energy"
        ]
    
    # Earth-Air
    elif (element1 == "earth" and element2 == "air") or (element1 == "air" and element2 == "earth"):
        return [
            "Ability to transform theoretical ideas into practical applications",
            "Balanced approach combining conceptual understanding with implementation",
            "Communication skills that explain complex concepts clearly",
            "Innovative problem-solving with practical constraints in mind",
            "Capacity to build systems based on sound principles"
        ], [
            "Use writing to bridge abstract thinking and practical planning",
            "Practice translating concepts into step-by-step plans",
            "Balance intellectual activities with hands-on projects",
            "Create systems for both exploration and application",
            "Recognize when to shift between thinking and doing"
        ]
    
    # Earth-Water
    elif (element1 == "earth" and element2 == "water") or (element1 == "water" and element2 == "earth"):
        return [
            "Ability to create emotionally supportive environments with practical foundations",
            "Natural talent for nurturing projects and relationships",
            "Intuitive understanding of material needs",
            "Capacity to build structures that honor emotional considerations",
            "Reliable emotional presence combined with practical support"
        ], [
            "Create daily practices that honor both emotional and practical needs",
            "Use journaling to explore feelings and material concerns",
            "Practice setting boundaries that protect well-being and resources",
            "Balance nurturing others with self-care",
            "Develop decision-making that integrates intuition with practical assessment"
        ]
    
    # Air-Water
    elif (element1 == "air" and element2 == "water") or (element1 == "water" and element2 == "air"):
        return [
            "Sophisticated emotional intelligence combining understanding with empathy",
            "Ability to articulate complex emotional experiences clearly",
            "Natural talent for psychological insight",
            "Creative expression that integrates concepts with emotional depth",
            "Capacity to move between objective analysis and subjective experience"
        ], [
            "Practice mindfulness to observe thoughts and emotions",
            "Use journaling to explore intellectual understanding and emotional experience",
            "Develop a personal language for emotional states",
            "Balance social interaction with emotional reflection",
            "Create decision-making processes that honor both logic and emotion"
        ]
    
    # Default return if no specific match
    return default_strengths, default_strategies

def generate_elements_tab_response(planets):
    """
    Generate a complete elements tab response structured for the UI.
    
    Args:
        planets: List of planet objects with sign information
        
    Returns:
        Dictionary with the complete elements tab data
    """
    # Step 1: Get basic element analysis
    element_analysis = analyze_elements(planets)
    
    # Step 2: Get element relationship data
    from .element_relationship_analyzer import analyze_element_relationships
    relationship_data = analyze_element_relationships(element_analysis['percentages'])
    
    # Step 3: Calculate conscious vs unconscious elements
    conscious_unconscious = separate_conscious_unconscious_elements(planets)
    
    # Step 4: Get element balance title
    balance_title = get_element_balance_title(element_analysis['percentages'])
    
    # Step 5: Format relationship data
    formatted_relationship = format_relationship_data(relationship_data)
    
    # Step 6: Get top two elements
    sorted_elements = sorted(element_analysis['percentages'].items(), key=lambda x: x[1], reverse=True)
    dominant_elements = [elem[0] for elem in sorted_elements[:2] if elem[1] > 20]
    
    # Step 7: Structure the response for UI
    return {
        "distribution": {
            "Fire": element_analysis['percentages']['fire'],
            "Earth": element_analysis['percentages']['earth'],
            "Air": element_analysis['percentages']['air'],
            "Water": element_analysis['percentages']['water'],
            "element_percentages": element_analysis.get('element_percentages', []),
            "dominant_elements": [element.capitalize() for element in dominant_elements],
            "title": balance_title,
            "description": element_analysis['description']['overall']
        },
        "relationship": formatted_relationship,
        "conscious_vs_unconscious": conscious_unconscious
    } 