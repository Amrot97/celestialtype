import os
import json
from geopy.geocoders import Nominatim
from pathlib import Path

def get_location(place_name):
    """Get geographic coordinates for a place name."""
    try:
        geolocator = Nominatim(user_agent="natal_chart_app")
        location = geolocator.geocode(place_name)
        if location:
            return location.latitude, location.longitude
        return None
    except Exception as e:
        print(f"Error getting location: {e}")
        return None

def extract_house_number(house_name):
    """Extract house number from house name."""
    try:
        if not house_name:
            return None
        
        # Handle different formats like "House 1", "1st House", etc.
        house_str = house_name.lower().replace("house", "").strip()
        
        # Remove ordinals
        for ordinal in ["st", "nd", "rd", "th"]:
            house_str = house_str.replace(ordinal, "")
        
        house_num = int(house_str.strip())
        return house_num
    except Exception:
        return None

def find_ephemeris_directory():
    """Find the ephemeris directory for Swiss Ephemeris."""
    try:
        # Check common locations
        possible_locations = [
            "./ephemeris",
            "../ephemeris",
            os.path.join(os.path.dirname(os.path.abspath(__file__)), "ephemeris"),
        ]
        
        for loc in possible_locations:
            if os.path.exists(loc) and os.path.isdir(loc):
                return os.path.abspath(loc)
                
        return None
    except Exception:
        return None

def extract_data_from_json_file(file_name):
    """Get data from a JSON file in the static_collection directory."""
    try:
        module_dir = os.path.dirname(os.path.abspath(__file__))
        static_collection_path = os.path.join(Path(module_dir).parent, "static_collection")
        json_file_path = os.path.join(static_collection_path, f"{file_name}.json")
        
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
        return data
    except Exception as e:
        print(f"Error extracting data from JSON file {file_name}: {str(e)}")
        return {}

def calculate_signs_power(planet_positions):
    """Calculate the power/influence of each sign based on planets positioned in them."""
    signs_power = {
        'Aries': 0, 'Taurus': 0, 'Gemini': 0, 'Cancer': 0, 
        'Leo': 0, 'Virgo': 0, 'Libra': 0, 'Scorpio': 0,
        'Sagittarius': 0, 'Capricorn': 0, 'Aquarius': 0, 'Pisces': 0
    }
    
    # Weights for different planets (Sun and Moon are more important)
    planet_weights = {
        'Sun': 3.0, 'Moon': 2.5, 
        'Mercury': 1.0, 'Venus': 1.0, 'Mars': 1.0,
        'Jupiter': 1.0, 'Saturn': 1.0,
        'Uranus': 0.5, 'Neptune': 0.5, 'Pluto': 0.5
    }
    
    # Calculate power for each sign
    for planet in planet_positions:
        planet_name = planet['planet']
        sign_name = planet['sign']['name']
        
        # Get weight for this planet (default to 0.5 if not in list)
        weight = planet_weights.get(planet_name, 0.5)
        
        # Add to sign's power
        if sign_name in signs_power:
            signs_power[sign_name] += weight
    
    return signs_power

def get_psychological_insights(planet_name, sign_name, house_number=None, title=""):
    """Generate psychological insights based on planet, sign, and house."""
    try:
        # Try to import the correct description module based on the planet name
        description = None
        
        # Import the specific sign description function based on the planet
        if planet_name.lower() == "sun":
            # Direct import from absolute path
            import os
            import sys
            import importlib.util
            
            module_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(module_dir, 'planet_descriptions', 'sun_sign_descriptions.py')
            
            spec = importlib.util.spec_from_file_location("sun_sign_descriptions", file_path)
            sun_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(sun_module)
            
            description = sun_module.get_sun_sign_description(sign_name)
            
        elif planet_name.lower() == "moon":
            # Direct import from absolute path
            import os
            import sys
            import importlib.util
            
            module_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(module_dir, 'planet_descriptions', 'moon_sign_descriptions.py')
            
            spec = importlib.util.spec_from_file_location("moon_sign_descriptions", file_path)
            moon_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(moon_module)
            
            description = moon_module.get_moon_sign_description(sign_name)
            
        elif planet_name.lower() == "venus":
            # Direct import from absolute path
            import os
            import sys
            import importlib.util
            
            module_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(module_dir, 'planet_descriptions', 'venus_sign_descriptions.py')
            
            spec = importlib.util.spec_from_file_location("venus_sign_descriptions", file_path)
            venus_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(venus_module)
            
            description = venus_module.get_venus_sign_description(sign_name)
            
        elif planet_name.lower() == "mars":
            # Direct import from absolute path
            import os
            import sys
            import importlib.util
            
            module_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(module_dir, 'planet_descriptions', 'mars_sign_descriptions.py')
            
            spec = importlib.util.spec_from_file_location("mars_sign_descriptions", file_path)
            mars_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mars_module)
            
            description = mars_module.get_mars_sign_description(sign_name)
            
        elif planet_name.lower() == "pluto":
            # Direct import from absolute path
            import os
            import sys
            import importlib.util
            
            module_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(module_dir, 'planet_descriptions', 'pluto_sign_descriptions.py')
            
            spec = importlib.util.spec_from_file_location("pluto_sign_descriptions", file_path)
            pluto_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(pluto_module)
            
            description = pluto_module.get_pluto_sign_description(sign_name)
            
        elif planet_name.lower() == "uranus":
            # Direct import from absolute path
            import os
            import sys
            import importlib.util
            
            module_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(module_dir, 'planet_descriptions', 'uranus_sign_descriptions.py')
            
            spec = importlib.util.spec_from_file_location("uranus_sign_descriptions", file_path)
            uranus_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(uranus_module)
            
            description = uranus_module.get_uranus_sign_description(sign_name)
            
        elif planet_name.lower() == "neptune":
            # Direct import from absolute path
            import os
            import sys
            import importlib.util
            
            module_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(module_dir, 'planet_descriptions', 'neptune_sign_descriptions.py')
            
            spec = importlib.util.spec_from_file_location("neptune_sign_descriptions", file_path)
            neptune_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(neptune_module)
            
            description = neptune_module.get_neptune_sign_description(sign_name)
        
        # If we have a description, use it; otherwise fall back to template
        if description:
            # Add house information if available
            explanation = None
            
            # For Venus and Mars, we need to handle different fields
            if planet_name.lower() == "venus":
                # Venus descriptions have strengths_in_connection and challenges_to_refine fields
                explanation = description.get("strengths_in_connection", "")
                if "challenges_to_refine" in description:
                    explanation += " " + description["challenges_to_refine"]
            elif planet_name.lower() == "mars":
                # Mars descriptions have strengths_in_action and challenges_to_navigate fields
                explanation = description.get("strengths_in_action", "")
                if "challenges_to_navigate" in description:
                    explanation += " " + description["challenges_to_navigate"]
            
            # For outer planets, they typically have explanation field
            elif planet_name.lower() in ["pluto", "uranus", "neptune"]:
                # Outer planets have collective_purpose and strengths fields
                explanation = description.get("collective_purpose", "")
                if "strengths" in description:
                    explanation += " " + description["strengths"]
            
            # For Sun and Moon, use the explanation field
            else:
                explanation = description.get("explanation", "")
                
            # If no explanation was found, use a placeholder
            if not explanation:
                explanation = f"This describes the influence of {planet_name} in {sign_name}"
                
            # Add house information
            if house_number:
                explanation += f" in House {house_number}"
            
            # Return the complete insight
            insight = {
                "planet": planet_name,
                "sign": sign_name,
                "house": house_number,
                "title": description.get("title", title or f"{planet_name} in {sign_name}"),
                "description": explanation,
                "keywords": description.get("keywords", ["placeholder", "keywords"])
            }
            
            return insight
        else:
            # Fallback to template for unsupported planets or signs
            if not planet_name or not sign_name:
                return None
            
            insight = {
                "planet": planet_name,
                "sign": sign_name,
                "house": house_number,
                "title": title or f"{planet_name} in {sign_name}",
                "description": f"This describes the influence of {planet_name} in {sign_name}",
                "keywords": ["placeholder", "keywords"]
            }
            
            if house_number:
                insight["description"] += f" in House {house_number}"
            
            return insight
    except ImportError as e:
        print(f"Could not import planet description module for {planet_name}: {str(e)}")
        # Fallback to template
        if not planet_name or not sign_name:
            return None
        
        insight = {
            "planet": planet_name,
            "sign": sign_name,
            "house": house_number,
            "title": title or f"{planet_name} in {sign_name}",
            "description": f"This describes the influence of {planet_name} in {sign_name}",
            "keywords": ["placeholder", "keywords"]
        }
        
        if house_number:
            insight["description"] += f" in House {house_number}"
        
        return insight
    except Exception as e:
        print(f"Error in get_psychological_insights for {planet_name}: {str(e)}")
        return None 