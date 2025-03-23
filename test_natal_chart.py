#!/usr/bin/env python
"""
Simple script to test the natal chart functionality.
"""
from immanuel import charts
from geopy.geocoders import Nominatim

def get_location(place_name):
    """Get latitude and longitude for a place name."""
    geolocator = Nominatim(user_agent="natal_chart_app")
    location = geolocator.geocode(place_name)
    if location:
        return location.latitude, location.longitude
    return None

def generate_natal_chart(name, date_of_birth, time_of_birth, place_of_birth):
    """Generate a natal chart for the given data."""
    coordinates = get_location(place_of_birth)
    if not coordinates:
        return {"error": "Could not determine location for the given place of birth."}

    latitude, longitude = coordinates
    datetime_of_birth = f"{date_of_birth} {time_of_birth}" if time_of_birth else f"{date_of_birth}"
    
    try:
        native = charts.Subject(datetime_of_birth, latitude, longitude)
        natal = charts.Natal(native)
        
        # Extract basic information
        result = {
            "name": name,
            "date_of_birth": date_of_birth,
            "time_of_birth": time_of_birth,
            "place_of_birth": place_of_birth,
            "coordinates": {"latitude": latitude, "longitude": longitude},
            "planets": {}
        }
        
        # Extract planet positions
        for obj_key in natal.objects:
            obj = natal.objects[obj_key]
            result["planets"][obj.name] = {
                "sign": obj.sign.name,
                "house": obj.house.name,
                "retrograde": obj.movement.retrograde if hasattr(obj, "movement") else None
            }
        
        return result
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    # Test with a sample birth data
    name = "Test User"
    date_of_birth = "1990-01-01"
    time_of_birth = "12:00:00"
    place_of_birth = "New York, USA"
    
    result = generate_natal_chart(name, date_of_birth, time_of_birth, place_of_birth)
    
    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print(f"Natal Chart for {result['name']}")
        print(f"Born on {result['date_of_birth']} at {result['time_of_birth']} in {result['place_of_birth']}")
        print(f"Coordinates: {result['coordinates']['latitude']}, {result['coordinates']['longitude']}")
        print("\nPlanet Positions:")
        for planet, data in result["planets"].items():
            retrograde = " (Retrograde)" if data["retrograde"] else ""
            print(f"{planet}: {data['sign']} in {data['house']}{retrograde}") 