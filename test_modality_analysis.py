import requests
import json

def test_modality_analysis():
    """Test the modality analysis functionality in the natal chart API."""
    url = "http://localhost:8000/natal-chart/"
    
    # Test data for a birth chart
    data = {
        "name": "Modality Test User",
        "date_of_birth": "1997-02-17",
        "place_of_birth": "Racibórz, Poland"
        # time_of_birth is omitted to test time-less chart
    }
    
    headers = {
        "Content-Type": "application/json",
        "X-Requested-With": "XMLHttpRequest"
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        print("Success! Natal chart with modality analysis generated.")
        result = response.json()
        
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
            print(f"Life Approach: {pattern['life_approach']}")
            print(f"Practical Advice: {pattern['practical_advice']}")
            
            # Print planets by modality
            planets_by_modality = result["modalityAnalysis"]["planets_by_modality"]
            print("\nPlanets by Modality:")
            for modality, planets in planets_by_modality.items():
                if planets:
                    print(f"  {modality}: {', '.join(planets)}")
            
            # Save the full response to a file
            with open("modality_analysis_response.json", "w") as f:
                json.dump(result, f, indent=2)
            print("\nFull response saved to modality_analysis_response.json")
        else:
            print("Error: Modality analysis not found in the response")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    test_modality_analysis() 