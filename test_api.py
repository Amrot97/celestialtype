#!/usr/bin/env python
"""
Script to test the natal chart API endpoint.
"""
import requests
import json

def test_natal_chart_api():
    """Test the natal chart API endpoint."""
    url = "http://localhost:8000/natal-chart/"
    data = {
        "name": "Test User",
        "date_of_birth": "1990-01-01",
        "time_of_birth": "12:00:00",
        "place_of_birth": "New York, USA"
    }
    
    headers = {
        'Content-Type': 'application/json',
        'X-Requested-With': 'XMLHttpRequest',  # This helps with CSRF exemption in Django
    }
    
    try:
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            print("Success! Natal chart generated.")
            result = response.json()
            print(f"User: {result.get('User_name')}")
            print(f"Date of Birth: {result.get('date_of_birth')}")
            print(f"Time of Birth: {result.get('time_of_birth')}")
            print(f"Place of Birth: {result.get('place_of_birth')}")
            print(f"Coordinates: {result.get('coordinates')}")
            
            # Print a few planet positions
            print("\nSample Planet Positions:")
            for planet in result.get('planet_positions', [])[:5]:  # Show first 5 planets
                print(f"{planet.get('planet')}: {planet.get('sign', {}).get('name')} in House {planet.get('house')}")
            
            # Save the full response to a file
            with open("natal_chart_response.json", "w") as f:
                json.dump(result, f, indent=2)
                print("\nFull response saved to natal_chart_response.json")
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    test_natal_chart_api() 