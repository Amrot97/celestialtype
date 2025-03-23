import requests
import json

def test_modality_with_time():
    """Test the modality analysis functionality in the natal chart API with birth time."""
    url = "http://localhost:8000/natal-chart/"
    
    # Test data for a birth chart with time
    data = {
        "name": "Modality Test With Time",
        "date_of_birth": "1997-02-17",
        "time_of_birth": "12:00:00",
        "place_of_birth": "Racibórz, Poland"
    }
    
    headers = {
        "Content-Type": "application/json",
        "X-Requested-With": "XMLHttpRequest"
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        print("Success! Natal chart with time and modality analysis generated.")
        result = response.json()
        
        # Check if time was provided in the response
        print(f"Time provided: {result.get('has_time', False)}")
        print(f"Time of birth: {result.get('time_of_birth', 'Not included')}")
        
        # Check if modality analysis is included
        if "modalityAnalysis" in result:
            print("\nModality Analysis:")
            
            # Print distribution
            distribution = result["modalityAnalysis"]["distribution"]
            print("\nModality Distribution:")
            for modality, percentage in distribution.items():
                print(f"  {modality}: {percentage:.1f}%")
            
            # Print pattern
            pattern = result["modalityAnalysis"]["pattern"]
            print(f"\nPattern Type: {pattern['pattern_type']}")
            print(f"Summary: {pattern['summary']}")
            
            # Print planets by modality
            planets_by_modality = result["modalityAnalysis"]["planets_by_modality"]
            print("\nPlanets by Modality:")
            for modality, planets in planets_by_modality.items():
                if planets:
                    print(f"  {modality}: {', '.join(planets)}")
            
            # Check if house stelliums are present
            has_house_stelliums = 'house_stelliums' in result.get('stelliums', {})
            print(f"\nHouse stelliums included: {has_house_stelliums}")
            
            # Save the full response to a file
            with open("modality_with_time_response.json", "w") as f:
                json.dump(result, f, indent=2)
            print("\nFull response saved to modality_with_time_response.json")
        else:
            print("Error: Modality analysis not found in the response")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    test_modality_with_time() 