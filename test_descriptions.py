#!/usr/bin/env python
"""
Test script for the natal chart API with file-based psychological insights.
"""
import requests
import json

def test_natal_chart_api():
    """Test the natal chart API endpoint with file-based psychological insights."""
    url = "http://localhost:8000/natal-chart/"
    data = {
        "name": "Test User",
        "date_of_birth": "1997-02-17",
        "time_of_birth": "12:00:00",
        "place_of_birth": "Racibórz, Poland"
    }
    
    headers = {
        'Content-Type': 'application/json',
        'X-Requested-With': 'XMLHttpRequest',
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
            
            # Print psychological insights
            print("\nPsychological Insights:")
            for insight in result.get('psychologicalInsights', []):
                print(f"\n{insight.get('title', 'Untitled')}")
                print(f"Planet: {insight.get('planet')} in {insight.get('sign')} (House {insight.get('house')})")
                print(f"Traits: {', '.join([trait.get('trait') for trait in insight.get('traits', [])])}")
                
                # Print a snippet of the description
                description = insight.get('description', '')
                if description:
                    snippet = description[:150] + "..." if len(description) > 150 else description
                    print(f"Description snippet: {snippet}")
            
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