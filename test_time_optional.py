import requests
import json

def test_with_time():
    """Test the natal chart API with time provided."""
    url = "http://localhost:8000/natal-chart/"
    
    data = {
        "name": "Test With Time",
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
        print("SUCCESS: Chart with time generated")
        result = response.json()
        
        # Check if time was provided in the response
        print(f"Time provided: {result.get('has_time', False)}")
        print(f"Time of birth: {result.get('time_of_birth', 'Not included')}")
        
        # Check if house data is present
        has_houses = any(p.get('house') is not None for p in result.get('planet_positions', []))
        print(f"Houses included: {has_houses}")
        
        # Check if house stelliums are present
        has_house_stelliums = 'house_stelliums' in result.get('stelliums', {})
        print(f"House stelliums included: {has_house_stelliums}")
        
        # Check if angles are present
        angles = ["Ascendant", "Descendant", "Midheaven", "Imum Coeli"]
        has_angles = any(p.get('planet') in angles for p in result.get('planet_positions', []))
        print(f"Angles included: {has_angles}")
        
        # Save response
        with open("chart_with_time.json", "w") as f:
            json.dump(result, f, indent=2)
        print("Full response saved to chart_with_time.json")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

def test_without_time():
    """Test the natal chart API without time provided."""
    url = "http://localhost:8000/natal-chart/"
    
    data = {
        "name": "Test Without Time",
        "date_of_birth": "1997-02-17",
        "place_of_birth": "Racibórz, Poland"
        # time_of_birth is omitted
    }
    
    headers = {
        "Content-Type": "application/json",
        "X-Requested-With": "XMLHttpRequest"
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        print("\nSUCCESS: Chart without time generated")
        result = response.json()
        
        # Check if time was provided in the response
        print(f"Time provided: {result.get('has_time', False)}")
        print(f"Time of birth: {result.get('time_of_birth', 'Not included')}")
        
        # Check if house data is present
        has_houses = any(p.get('house') is not None for p in result.get('planet_positions', []))
        print(f"Houses included: {has_houses}")
        
        # Check if house stelliums are present
        has_house_stelliums = 'house_stelliums' in result.get('stelliums', {})
        print(f"House stelliums included: {has_house_stelliums}")
        
        # Check if angles are present
        angles = ["Ascendant", "Descendant", "Midheaven", "Imum Coeli"]
        has_angles = any(p.get('planet') in angles for p in result.get('planet_positions', []))
        print(f"Angles included: {has_angles}")
        
        # Check if sign stelliums are present
        has_sign_stelliums = 'sign_stelliums' in result.get('stelliums', {})
        print(f"Sign stelliums included: {has_sign_stelliums}")
        
        # Save response
        with open("chart_without_time.json", "w") as f:
            json.dump(result, f, indent=2)
        print("Full response saved to chart_without_time.json")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    test_with_time()
    test_without_time() 