def detect_stelliums(planets, min_planets=3, include_points=False, tight_orb=False):
    """
    Detect stelliums in a birth chart.
    A stellium is a group of planets in the same sign or house.
    
    Args:
        planets: List of planet objects with sign and house information
        min_planets: Minimum number of planets to consider as a stellium
        include_points: Whether to include points like North Node in stellium calculation
        tight_orb: Whether to check for tighter orb (planets within 8 degrees)
        
    Returns:
        Dictionary with detected stelliums
    """
    # Initialize counters for signs and houses
    sign_counts = {}
    house_counts = {}
    
    # Track which planets are in each sign and house
    planets_in_sign = {}
    planets_in_house = {}
    
    # Track positions for tight orb calculation
    planet_positions = {}
    
    # List of major planets (exclude points unless specified)
    major_planets = ["Sun", "Moon", "Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
    if include_points:
        major_planets.extend(["North Node", "South Node", "Ascendant", "Midheaven"])
    
    # Process each planet
    for planet_data in planets:
        # Get planet name (handle different formats)
        planet_name = planet_data.get("name", planet_data.get("planet", ""))
        
        # Skip if not a recognized planet or if we're excluding points
        if not planet_name or (not include_points and planet_name not in major_planets):
            continue
            
        # Get sign information
        sign_name = None
        if isinstance(planet_data.get("sign"), dict):
            sign_name = planet_data.get("sign", {}).get("name", "")
        else:
            sign_name = planet_data.get("sign", "")
            
        # Get house information
        house_number = planet_data.get("house")
        
        # Get position for tight orb calculation
        position = None
        if tight_orb and "position" in planet_data:
            pos = planet_data["position"]
            degrees = pos.get("degrees", 0)
            minutes = pos.get("minutes", 0) / 60  # Convert to decimal degrees
            total_degrees = degrees + minutes
            
            # Store the position
            position = total_degrees
        
        # Count signs
        if sign_name:
            sign_counts[sign_name] = sign_counts.get(sign_name, 0) + 1
            
            if sign_name not in planets_in_sign:
                planets_in_sign[sign_name] = []
                
            planets_in_sign[sign_name].append({
                "name": planet_name,
                "position": position
            })
        
        # Count houses (if available)
        if house_number:
            house_key = f"House {house_number}"
            house_counts[house_key] = house_counts.get(house_key, 0) + 1
            
            if house_key not in planets_in_house:
                planets_in_house[house_key] = []
                
            planets_in_house[house_key].append({
                "name": planet_name,
                "position": position
            })
    
    # Find stelliums (groups of 3+ planets)
    sign_stelliums = []
    house_stelliums = []
    
    # Check for sign stelliums
    for sign, count in sign_counts.items():
        if count >= min_planets:
            # Get the planets in this sign
            planets_list = planets_in_sign[sign]
            
            # If using tight orb, check planet proximity
            if tight_orb:
                # Check if at least min_planets are within 8 degrees of each other
                tight_groups = find_tight_groups(planets_list, 8)
                
                # Only include if we have tight groups
                if tight_groups:
                    for group in tight_groups:
                        if len(group) >= min_planets:
                            sign_stelliums.append({
                                "type": "sign",
                                "location": sign,
                                "count": len(group),
                                "planets": [p["name"] for p in group],
                                "tight": True
                            })
            else:
                # Just include all planets in the sign
                sign_stelliums.append({
                    "type": "sign",
                    "location": sign,
                    "count": count,
                    "planets": [p["name"] for p in planets_list],
                    "tight": False
                })
    
    # Check for house stelliums
    for house, count in house_counts.items():
        if count >= min_planets:
            # Get the planets in this house
            planets_list = planets_in_house[house]
            
            # If using tight orb, check planet proximity
            if tight_orb:
                # Check if at least min_planets are within 8 degrees of each other
                tight_groups = find_tight_groups(planets_list, 8)
                
                # Only include if we have tight groups
                if tight_groups:
                    for group in tight_groups:
                        if len(group) >= min_planets:
                            house_stelliums.append({
                                "type": "house",
                                "location": house,
                                "count": len(group),
                                "planets": [p["name"] for p in group],
                                "tight": True
                            })
            else:
                # Just include all planets in the house
                house_stelliums.append({
                    "type": "house",
                    "location": house,
                    "count": count,
                    "planets": [p["name"] for p in planets_list],
                    "tight": False
                })
    
    # Return the results
    return {
        "sign_stelliums": sign_stelliums,
        "house_stelliums": house_stelliums
    }

def detect_sign_stelliums_only(planets, min_planets=3, include_points=False, tight_orb=False):
    """
    Detect sign stelliums in a birth chart (for charts without time).
    
    Args:
        planets: List of planet objects with sign information
        min_planets: Minimum number of planets to consider as a stellium
        include_points: Whether to include points like North Node in stellium calculation
        tight_orb: Whether to check for tighter orb (planets within 8 degrees)
        
    Returns:
        Dictionary with detected stelliums
    """
    # Initialize counters for signs
    sign_counts = {}
    planets_in_sign = {}
    
    # List of major planets (exclude points unless specified)
    major_planets = ["Sun", "Moon", "Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
    if include_points:
        major_planets.extend(["North Node", "South Node"])
    
    # Process each planet
    for planet_data in planets:
        # Get planet name (handle different formats)
        planet_name = planet_data.get("name", planet_data.get("planet", ""))
        
        # Skip if not a recognized planet or if we're excluding points
        if not planet_name or (not include_points and planet_name not in major_planets):
            continue
            
        # Get sign information
        sign_name = None
        if isinstance(planet_data.get("sign"), dict):
            sign_name = planet_data.get("sign", {}).get("name", "")
        else:
            sign_name = planet_data.get("sign", "")
            
        # Get position for tight orb calculation
        position = None
        if tight_orb and "position" in planet_data:
            pos = planet_data["position"]
            degrees = pos.get("degrees", 0)
            minutes = pos.get("minutes", 0) / 60  # Convert to decimal degrees
            total_degrees = degrees + minutes
            
            # Store the position
            position = total_degrees
        
        # Count signs
        if sign_name:
            sign_counts[sign_name] = sign_counts.get(sign_name, 0) + 1
            
            if sign_name not in planets_in_sign:
                planets_in_sign[sign_name] = []
                
            planets_in_sign[sign_name].append({
                "name": planet_name,
                "position": position
            })
    
    # Find stelliums (groups of 3+ planets)
    sign_stelliums = []
    
    # Check for sign stelliums
    for sign, count in sign_counts.items():
        if count >= min_planets:
            # Get the planets in this sign
            planets_list = planets_in_sign[sign]
            
            # If using tight orb, check planet proximity
            if tight_orb:
                # Check if at least min_planets are within 8 degrees of each other
                tight_groups = find_tight_groups(planets_list, 8)
                
                # Only include if we have tight groups
                if tight_groups:
                    for group in tight_groups:
                        if len(group) >= min_planets:
                            sign_stelliums.append({
                                "type": "sign",
                                "location": sign,
                                "count": len(group),
                                "planets": [p["name"] for p in group],
                                "tight": True
                            })
            else:
                # Just include all planets in the sign
                sign_stelliums.append({
                    "type": "sign",
                    "location": sign,
                    "count": count,
                    "planets": [p["name"] for p in planets_list],
                    "tight": False
                })
    
    # Return the results
    return {
        "sign_stelliums": sign_stelliums,
        "house_stelliums": []  # Empty for charts without time
    }

def find_tight_groups(planets, max_orb):
    """
    Find groups of planets that are within the specified orb (degree difference).
    
    Args:
        planets: List of planet dictionaries with position information
        max_orb: Maximum orb in degrees
        
    Returns:
        List of planet groups that are within the specified orb
    """
    # Filter out planets without position data
    planets_with_pos = [p for p in planets if p.get("position") is not None]
    
    # If not enough planets have position data, return None
    if len(planets_with_pos) < 2:
        return None
        
    # Sort planets by position
    sorted_planets = sorted(planets_with_pos, key=lambda p: p["position"])
    
    # Find connected groups
    groups = []
    current_group = [sorted_planets[0]]
    
    for i in range(1, len(sorted_planets)):
        current_planet = sorted_planets[i]
        previous_planet = sorted_planets[i-1]
        
        # Calculate the orb
        orb = current_planet["position"] - previous_planet["position"]
        
        # Handle case where planets cross from Pisces to Aries (0° boundary)
        if orb > 30:
            orb = 30 - (current_planet["position"] % 30)
        
        if orb <= max_orb:
            # Part of the current group
            current_group.append(current_planet)
        else:
            # Start a new group if the current one has more than 1 planet
            if len(current_group) > 1:
                groups.append(current_group)
            current_group = [current_planet]
    
    # Add the last group if it has more than 1 planet
    if len(current_group) > 1:
        groups.append(current_group)
    
    return groups

def get_stellium_descriptions(stelliums):
    """
    Generate descriptions for detected stelliums.
    
    Args:
        stelliums: Dictionary with detected stelliums
        
    Returns:
        List of simplified stellium descriptions
    """
    descriptions = []
    
    # Process sign stelliums
    for stellium in stelliums.get("sign_stelliums", []):
        location = stellium["location"]
        count = stellium["count"]
        planets = stellium["planets"]
        
        # Create simplified description
        description = {
            "planets": planets,
            "title": f"{count} Planets in {location}",
            "subtitle": f"{'Tight ' if stellium.get('tight') else ''}Sign Stellium",
            "text": generate_sign_stellium_text(location, planets)
        }
        
        descriptions.append(description)
    
    # Process house stelliums
    for stellium in stelliums.get("house_stelliums", []):
        location = stellium["location"]
        count = stellium["count"]
        planets = stellium["planets"]
        
        # Create simplified description
        description = {
            "planets": planets,
            "title": f"{count} Planets in {location}",
            "subtitle": f"{'Tight ' if stellium.get('tight') else ''}House Stellium",
            "text": generate_house_stellium_text(location, planets)
        }
        
        descriptions.append(description)
    
    return descriptions

def get_sign_stellium_descriptions_only(stelliums):
    """
    Generate descriptions for detected sign stelliums (for charts without time).
    
    Args:
        stelliums: Dictionary with detected stelliums
        
    Returns:
        List of simplified stellium descriptions
    """
    descriptions = []
    
    # Process sign stelliums
    for stellium in stelliums.get("sign_stelliums", []):
        location = stellium["location"]
        count = stellium["count"]
        planets = stellium["planets"]
        
        # Create simplified description
        description = {
            "planets": planets,
            "title": f"{count} Planets in {location}",
            "subtitle": f"{'Tight ' if stellium.get('tight') else ''}Sign Stellium",
            "text": generate_sign_stellium_text(location, planets)
        }
        
        descriptions.append(description)
    
    return descriptions

def generate_sign_stellium_text(sign, planets):
    """Generate description text for a sign stellium."""
    # List of planets in text form
    planet_text = ", ".join(planets[:-1]) + " and " + planets[-1] if len(planets) > 1 else planets[0]
    
    # Generate basic description
    text = f"You have a concentration of {planet_text} in {sign}. "
    
    # Add sign-specific descriptions
    sign_descriptions = {
        "Aries": "This gives you a strong pioneering spirit, courage, and initiative. You may approach life with enthusiasm and are not afraid to start new ventures.",
        "Taurus": "This gives you a strong drive for security, stability, and material comfort. You likely have a practical approach to life and value reliability.",
        "Gemini": "This gives you exceptional communication skills, curiosity, and mental agility. You thrive on variety and may have diverse interests.",
        "Cancer": "This gives you deep emotional sensitivity, nurturing qualities, and a strong connection to home and family. Your intuition is likely very developed.",
        "Leo": "This gives you natural leadership, creativity, and self-expression. You shine brightly and may have a dramatic flair in how you present yourself.",
        "Virgo": "This gives you analytical precision, attention to detail, and a service-oriented approach. You excel at improving systems and solving practical problems.",
        "Libra": "This gives you a strong focus on relationships, harmony, and balance. You have a natural diplomatic ability and aesthetic sensibility.",
        "Scorpio": "This gives you emotional intensity, psychological depth, and transformative power. You may have strong investigative abilities and regenerative capacity.",
        "Sagittarius": "This gives you a philosophical outlook, love of freedom, and expansive vision. You seek meaning and growth through exploration.",
        "Capricorn": "This gives you ambition, discipline, and strong executive abilities. You approach goals methodically and can achieve significant long-term success.",
        "Aquarius": "This gives you innovative thinking, humanitarian values, and a unique perspective. You may be ahead of your time in your ideas.",
        "Pisces": "This gives you exceptional imagination, compassion, and spiritual sensitivity. You have a connection to collective consciousness and artistic inspiration."
    }
    
    # Add the sign-specific text
    text += sign_descriptions.get(sign, "This creates a powerful focus in your chart in this area.")
    
    # Add stellium impact
    text += " Having multiple planets in one sign creates an emphasis on these qualities in your personality and life experience."
    
    return text

def generate_house_stellium_text(house, planets):
    """Generate description text for a house stellium."""
    # Extract house number
    house_num = int(house.replace("House ", "")) if "House " in house else 0
    
    # List of planets in text form
    planet_text = ", ".join(planets[:-1]) + " and " + planets[-1] if len(planets) > 1 else planets[0]
    
    # Generate basic description
    text = f"You have a concentration of {planet_text} in your {house}. "
    
    # Add house-specific descriptions
    house_descriptions = {
        1: "This puts significant focus on your identity, appearance, and how you initiate action. This area of life is highly energized for you.",
        2: "This emphasizes financial matters, personal resources, and values. Your attention and energy are directed toward building security and managing resources.",
        3: "This highlights communication, learning, and your immediate environment. You likely put significant energy into expressing ideas and connecting with others.",
        4: "This concentrates energy in your home, family, and emotional foundations. Your private life and sense of belonging are major themes.",
        5: "This emphasizes creativity, self-expression, romance, and pleasure. This area is highly activated, bringing focus to your creative and recreational pursuits.",
        6: "This puts focus on work, health, and service. Your daily routines, skills development, and how you help others are significant themes.",
        7: "This highlights partnerships, cooperation, and one-on-one relationships. Your interactions with others and how you balance yourself through relationships are emphasized.",
        8: "This concentrates energy in areas of shared resources, transformation, and psychological depth. Issues of power, intimacy, and regeneration are significant.",
        9: "This emphasizes higher education, philosophy, travel, and belief systems. Your quest for meaning and broad horizons is a major theme.",
        10: "This puts focus on career, public reputation, and life direction. Your ambitions and how you contribute to society are highly energized.",
        11: "This highlights friendships, groups, and humanitarian ideals. Your social networks and vision for the future are significant themes.",
        12: "This concentrates energy in the unconscious, spiritual pursuits, and hidden influences. Your inner world and connection to the universal are emphasized."
    }
    
    # Add the house-specific text
    text += house_descriptions.get(house_num, "This creates a powerful focus in this area of your life.")
    
    # Add stellium impact
    text += " Having multiple planets in one house creates an emphasis on these life themes and makes this area particularly significant in your experience."
    
    return text 