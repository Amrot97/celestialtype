"""
Element descriptions and templates for natal chart analysis.
Provides detailed insights into elemental balance and its practical implications.
"""

# Import necessary modules
import json

# Define the basic structure for element descriptions
ELEMENT_DESCRIPTIONS = {
    "Fire": {
        "title": "Fire Element (Aries, Leo, Sagittarius)",
        "core_traits": "Initiative, passion, creativity, inspiration, dynamic expression",
        "description": "Fire represents the transformative power of spirit in action. In the natural world, fire converts matter into energy, and similarly, your Fire element transforms ideas into dynamic expression. This elemental force governs inspiration, creative drive, and the courage to initiate change.",
        "high_description": "With strong Fire element, you naturally energize and inspire those around you. Your enthusiasm is contagious, and you excel at initiating projects and motivating others. You're likely the person who sparks new ideas in meetings, leads community initiatives, or inspires friends to pursue their dreams.",
        "high_strengths": [
            "Natural ability to inspire and motivate others through authentic enthusiasm",
            "Quick to recognize and seize opportunities for growth and advancement",
            "Creative vision that can transform abstract ideas into concrete action",
            "Courage to take initiative and lead others into new territory"
        ],
        "high_challenges": [
            "Risk of burning out from maintaining too high an energy level",
            "May overwhelm others with intensity or rapid-fire ideas",
            "Tendency to start projects without sufficient planning for follow-through",
            "Can become frustrated with slower, more methodical processes"
        ],
        "low_description": "With minimal Fire element, you may find it challenging to access spontaneous energy, enthusiasm, and self-motivated action. You might approach life with more caution and deliberation than immediate passion.",
        "low_challenges": [
            "Difficulty initiating action without external motivation",
            "May struggle with self-confidence and assertiveness",
            "Can find it hard to express enthusiasm or passion openly",
            "Might avoid risks or competitive situations"
        ],
        "development_strategies": [
            "Schedule regular physical activity to stimulate natural fire energy",
            "Practice small acts of spontaneity in low-risk situations",
            "Set achievable goals that require initiative and celebrate their completion",
            "Explore creative activities that encourage self-expression"
        ]
    },
    "Earth": {
        "title": "Earth Element (Taurus, Virgo, Capricorn)",
        "core_traits": "Stability, practicality, manifestation, resourcefulness, material wisdom",
        "description": "Earth represents the power of manifestation and form. In the natural world, earth provides structure and nourishment, and similarly, your Earth element brings ideas into tangible reality. This elemental force governs practical wisdom, resource management, and the ability to create lasting foundations.",
        "high_description": "With strong Earth element, you naturally excel at bringing ideas into form and creating tangible results. Your grounded presence provides stability and reliability that others depend upon. You're likely the person who turns visions into step-by-step plans and builds lasting structures.",
        "high_strengths": [
            "Natural ability to manifest ideas into tangible results",
            "Excellence in resource management and practical planning",
            "Strong sense of timing and patience in building foundations",
            "Reliability that creates trust and stability in all endeavors"
        ],
        "high_challenges": [
            "Risk of becoming too rigid or resistant to change",
            "May prioritize security over growth opportunities",
            "Tendency to stay in comfort zone rather than take risks",
            "Can become overly focused on material aspects"
        ],
        "low_description": "With minimal Earth element, you may find it challenging to ground ideas in practical reality and create stable foundations. You might approach life with more theoretical or emotional perspectives than practical considerations.",
        "low_challenges": [
            "Difficulty completing projects and following through on plans",
            "May struggle with practical matters like finances and organization",
            "Can find it hard to establish routines and consistent habits",
            "Might avoid dealing with material world responsibilities"
        ],
        "development_strategies": [
            "Create simple daily routines to build consistency",
            "Practice completing one small project before starting another",
            "Develop a relationship with nature through gardening or hiking",
            "Learn basic financial management and organizational skills"
        ]
    },
    "Air": {
        "title": "Air Element (Gemini, Libra, Aquarius)",
        "core_traits": "Intelligence, communication, social connection, innovation, mental clarity",
        "description": "Air represents the power of thought and connection. In the natural world, air facilitates exchange and movement, and similarly, your Air element enables the flow of ideas and social bonds. This elemental force governs intellectual understanding, communication, and the ability to see multiple perspectives.",
        "high_description": "With strong Air element, you naturally excel at processing information and connecting ideas. Your intellectual agility and communication skills make you a natural networker and innovator. You're likely the person who sees unique patterns and develops innovative solutions.",
        "high_strengths": [
            "Natural ability to process and synthesize complex information",
            "Excellence in communication and idea exchange",
            "Strong capacity for objective analysis and fair judgment",
            "Talent for seeing patterns and making unique connections"
        ],
        "high_challenges": [
            "Risk of becoming too detached from emotions and physical needs",
            "May overthink situations rather than taking action",
            "Tendency to live in theoretical rather than practical realms",
            "Can become scattered when pursuing too many interests"
        ],
        "low_description": "With minimal Air element, you may find it challenging to detach from personal feelings to gain objective perspective. You might approach life with more emotional or practical considerations than intellectual analysis.",
        "low_challenges": [
            "Difficulty seeing multiple perspectives in complex situations",
            "May struggle with abstract thinking and theoretical concepts",
            "Can find it hard to articulate thoughts and ideas clearly",
            "Might avoid intellectual discussions or social networking"
        ],
        "development_strategies": [
            "Engage in regular reading across diverse topics",
            "Practice writing to clarify and express thoughts",
            "Join discussion groups or take classes that encourage intellectual exchange",
            "Develop listening skills to better understand different perspectives"
        ]
    },
    "Water": {
        "title": "Water Element (Cancer, Scorpio, Pisces)",
        "core_traits": "Emotion, intuition, empathy, healing, creative flow",
        "description": "Water represents the power of feeling and intuitive wisdom. In the natural world, water flows, nurtures, and transforms, and similarly, your Water element enables emotional depth and healing connections. This elemental force governs empathy, creativity, and the ability to navigate the depths of human experience.",
        "high_description": "With strong Water element, you naturally excel at understanding emotional currents and offering empathetic support. Your intuitive sensitivity and emotional intelligence make you a natural healer and creative force. You're likely the person others turn to for emotional support.",
        "high_strengths": [
            "Natural ability to understand and process complex emotions",
            "Deep intuitive wisdom and psychic sensitivity",
            "Strong capacity for empathy and emotional support",
            "Talent for creative expression and artistic flow"
        ],
        "high_challenges": [
            "Risk of absorbing others' emotions and energy",
            "May become overwhelmed by emotional intensity",
            "Tendency to avoid conflict or difficult feelings",
            "Can struggle with maintaining clear boundaries"
        ],
        "low_description": "With minimal Water element, you may find it challenging to access emotional depth, intuitive wisdom, and empathic connection. You might approach feelings with more analysis or practicality than direct experience.",
        "low_challenges": [
            "Difficulty recognizing and processing emotions as they arise",
            "May struggle with empathy and emotional connection",
            "Can find it hard to access intuition or trust inner knowing",
            "Might avoid emotional vulnerability or intimate sharing"
        ],
        "development_strategies": [
            "Keep an emotion journal to develop greater emotional awareness",
            "Practice mindfulness meditation focused on bodily sensations",
            "Engage with water-based activities like swimming or bathing rituals",
            "Explore creative arts that encourage emotional expression"
        ]
    }
}

# Define pattern templates for overall analysis
OVERALL_PATTERN_TEMPLATES = {
    "balanced": {
        "title": "Balanced Elemental Distribution",
        "description": "Your chart shows a harmonious balance between all elements, indicating a well-rounded approach to life. You can easily adapt to different situations, drawing on practical stability (Earth), emotional intelligence (Water), mental clarity (Air), and passionate drive (Fire) as needed.",
        "strengths": [
            "Natural adaptability",
            "Balanced perspective",
            "Multiple problem-solving approaches",
            "Well-rounded skill set",
            "Versatility in different situations"
        ],
        "development_areas": [
            "Maintain the existing balance",
            "Recognize when to emphasize different elements",
            "Learn to consciously shift between approaches",
            "Develop expertise while maintaining versatility",
            "Help others find their balance"
        ]
    },
    "fire_dominant": {
        "title": "Fire Element Emphasis",
        "description": "Your chart shows a strong emphasis on the Fire element, highlighting your natural enthusiasm, creativity, and leadership qualities. This configuration brings dynamic energy and inspiring vision to your life path.",
        "strengths": [
            "Natural leadership",
            "Creative vision",
            "Passionate drive",
            "Inspiring presence",
            "Quick action"
        ],
        "development_areas": [
            "Cultivate patience",
            "Develop grounding practices",
            "Balance action with reflection",
            "Consider practical details",
            "Practice emotional awareness"
        ]
    },
    "earth_dominant": {
        "title": "Earth Element Emphasis",
        "description": "Your chart emphasizes the Earth element, indicating a strong practical nature and ability to manifest in the material world. This configuration supports stability, reliability, and steady progress toward goals.",
        "strengths": [
            "Practical wisdom",
            "Material success",
            "Reliability",
            "Resource management",
            "Building foundations"
        ],
        "development_areas": [
            "Embrace flexibility",
            "Explore creativity",
            "Develop emotional expression",
            "Consider abstract ideas",
            "Practice spontaneity"
        ]
    },
    "air_dominant": {
        "title": "Air Element Emphasis",
        "description": "Your chart shows a strong Air element emphasis, highlighting your intellectual nature and communication abilities. This configuration supports innovation, social connections, and analytical thinking.",
        "strengths": [
            "Mental clarity",
            "Communication skills",
            "Social networking",
            "Innovation",
            "Analytical ability"
        ],
        "development_areas": [
            "Ground ideas in practice",
            "Develop emotional awareness",
            "Connect with physical body",
            "Build stability",
            "Balance thinking with feeling"
        ]
    },
    "water_dominant": {
        "title": "Water Element Emphasis",
        "description": "Your chart emphasizes the Water element, indicating deep emotional intelligence and intuitive abilities. This configuration supports empathy, creativity, and healing capacities.",
        "strengths": [
            "Emotional depth",
            "Intuitive wisdom",
            "Empathy",
            "Healing ability",
            "Creative expression"
        ],
        "development_areas": [
            "Establish boundaries",
            "Develop practical skills",
            "Balance emotion with logic",
            "Build structure",
            "Practice objectivity"
        ]
    },
    "fire_earth_emphasis": {
        "title": "Fire-Earth Emphasis",
        "description": "Your chart shows a strong combination of Fire and Earth elements, blending practical ability with creative drive. This configuration supports manifesting vision into reality.",
        "strengths": [
            "Practical creativity",
            "Driven manifestation",
            "Energetic stability",
            "Resourceful action",
            "Grounded leadership"
        ],
        "development_areas": [
            "Develop emotional awareness",
            "Practice flexibility",
            "Enhance communication",
            "Balance action with reflection",
            "Consider others' perspectives"
        ]
    },
    "air_water_emphasis": {
        "title": "Air-Water Emphasis",
        "description": "Your chart combines strong Air and Water elements, integrating intellectual and emotional intelligence. This configuration supports innovative emotional understanding and creative communication.",
        "strengths": [
            "Emotional intelligence",
            "Creative thinking",
            "Intuitive communication",
            "Empathetic understanding",
            "Artistic expression"
        ],
        "development_areas": [
            "Build practical foundations",
            "Develop consistency",
            "Ground ideas in reality",
            "Balance analysis with action",
            "Create stable structures"
        ]
    }
}

def get_element_description(element, include_high_descriptions=True, include_low_descriptions=True):
    """
    Retrieves the description for a specific element.
    
    Parameters:
    - element (str): Name of the element (e.g., "Fire", "Earth", "Air", "Water")
    - include_high_descriptions (bool): Whether to include descriptions for high element presence
    - include_low_descriptions (bool): Whether to include descriptions for low element presence
    
    Returns:
    - dict: Formatted element description or None if not found
    """
    # Handle invalid input
    if not isinstance(element, str):
        return None
    
    # Normalize the element name (capitalize first letter)
    try:
        element = element.capitalize()
    except AttributeError:
        return None
    
    # Get the description
    description = ELEMENT_DESCRIPTIONS.get(element)
    if not description:
        return None
        
    # Format the response
    result = {
        "title": description["title"],
        "core_traits": description.get("core_traits", ""),
        "description": description.get("description", "")
    }
    
    # Add high descriptions if requested
    if include_high_descriptions:
        result.update({
            "high_description": description.get("high_description", ""),
            "high_strengths": description.get("high_strengths", []),
            "high_challenges": description.get("high_challenges", [])
        })
    
    # Add low descriptions if requested
    if include_low_descriptions:
        result.update({
            "low_description": description.get("low_description", ""),
            "low_challenges": description.get("low_challenges", []),
            "development_strategies": description.get("development_strategies", [])
        })
    
    return result

def get_pattern_template(pattern_key):
    """
    Retrieve the template for a specific elemental pattern.
    
    Args:
        pattern_key (str): Key for the pattern template
    
    Returns:
        dict: Template dictionary for the specified pattern
    """
    # Handle invalid input
    if not isinstance(pattern_key, str):
        return {}
    
    try:
        return OVERALL_PATTERN_TEMPLATES.get(pattern_key, {})
    except (TypeError, KeyError):
        return {}

def get_elemental_balance_analysis(element_percentages):
    """
    Analyzes the elemental balance and provides practical interpretations.
    
    Parameters:
    - element_percentages (dict): Percentages for each element (Fire, Earth, Air, Water)
    
    Returns:
    - dict: Detailed analysis of elemental balance including:
        - Dominant elements
        - Moderate elements
        - Lacking elements
        - Overall pattern interpretation
        - Practical advice for balance
    """
    # Handle invalid input
    if not isinstance(element_percentages, dict):
        return {
            "pattern": get_pattern_template("balanced"),
            "dominant_elements": [],
            "moderate_elements": [],
            "lacking_elements": [],
            "is_balanced": True,
            "percentages": {"Fire": 25.0, "Earth": 25.0, "Air": 25.0, "Water": 25.0}
        }
    
    # Validate and clean input
    valid_elements = {"Fire", "Earth", "Air", "Water"}
    cleaned_percentages = {}
    
    for element in valid_elements:
        try:
            value = float(element_percentages.get(element, 25.0))
            # Clamp value between 0 and 100
            cleaned_percentages[element] = max(0.0, min(100.0, value))
        except (ValueError, TypeError):
            cleaned_percentages[element] = 25.0
    
    # Normalize percentages to sum to 100
    total = sum(cleaned_percentages.values())
    if total > 0:
        for element in cleaned_percentages:
            cleaned_percentages[element] = (cleaned_percentages[element] / total) * 100
    
    # Define thresholds for interpretation
    HIGH_THRESHOLD = 30  # Lowered from 35
    LOW_THRESHOLD = 20   # Raised from 15
    EXTREME_THRESHOLD = 40  # Lowered from 50
    VERY_LOW_THRESHOLD = 10  # Raised from 5
    
    # Determine dominant, moderate, and lacking elements
    dominant = [e for e, v in cleaned_percentages.items() if v >= HIGH_THRESHOLD]
    lacking = [e for e, v in cleaned_percentages.items() if v <= LOW_THRESHOLD]
    moderate = [e for e, v in cleaned_percentages.items() if LOW_THRESHOLD < v < HIGH_THRESHOLD]
    
    # Identify extreme cases
    extreme_dominant = [e for e, v in cleaned_percentages.items() if v >= EXTREME_THRESHOLD]
    very_lacking = [e for e, v in cleaned_percentages.items() if v <= VERY_LOW_THRESHOLD]
    
    # Check for balanced distribution
    values = list(cleaned_percentages.values())
    max_diff = max(values) - min(values)
    is_balanced = max_diff < 20  # Increased from 15
    
    # Determine overall pattern
    pattern_key = "balanced"
    if is_balanced:
        pattern_key = "balanced"
    elif len(extreme_dominant) == 1:
        pattern_key = f"{extreme_dominant[0].lower()}_dominant"
    elif len(dominant) == 2:
        elements = sorted([e.lower() for e in dominant])
        pattern_key = f"{elements[0]}_{elements[1]}_emphasis"
    elif len(dominant) == 1:
        pattern_key = f"{dominant[0].lower()}_dominant"
    
    # Get pattern template
    pattern = get_pattern_template(pattern_key)
    
    # Get descriptions for elements
    dominant_elements = []
    for e in dominant:
        desc = get_element_description(e, include_high_descriptions=True, include_low_descriptions=False)
        if desc:
            if e in extreme_dominant:
                desc["level"] = "very high"
            else:
                desc["level"] = "high"
            dominant_elements.append(desc)
    
    # Get descriptions for moderate elements
    moderate_elements = []
    for e in moderate:
        desc = get_element_description(e, include_high_descriptions=True, include_low_descriptions=True)
        if desc:
            desc["level"] = "moderate"
            moderate_elements.append(desc)
    
    # Add descriptions for lacking elements with appropriate level indicators
    lacking_elements = []
    for element in lacking:
        desc = get_element_description(element, include_high_descriptions=False, include_low_descriptions=True)
        if desc:
            if element in very_lacking:
                desc["level"] = "very low"
            else:
                desc["level"] = "low"
            lacking_elements.append(desc)
    
    # Build analysis
    analysis = {
        "pattern": pattern,
        "dominant_elements": dominant_elements,
        "moderate_elements": moderate_elements,
        "lacking_elements": lacking_elements,
        "is_balanced": is_balanced,
        "percentages": cleaned_percentages,
    }
    
    return analysis
