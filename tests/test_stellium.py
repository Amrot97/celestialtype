#!/usr/bin/env python
"""
Test script for the natal chart API with stellium detection.
"""
import requests
import json

def test_stellium_detection():
    """
    Test the stellium detection functionality in the natal chart API.
    """
    # Test data for a birth chart that should have a stellium in Aquarius
    test_data = {
        "name": "Test User",
        "date_of_birth": "1997-02-17",
        "time_of_birth": "12:00:00",
        "place_of_birth": "Racibórz, Poland"
    }
    
    # Headers for CSRF exemption
    headers = {
        "Content-Type": "application/json",
        "X-Requested-With": "XMLHttpRequest"
    }
    
    # Send the request to the API
    response = requests.post(
        "http://localhost:8000/natal-chart/",
        data=json.dumps(test_data),
        headers=headers
    )
    
    # Check if the request was successful
    if response.status_code == 200:
        print("Success! Natal chart generated.")
        data = response.json()
        
        # Print user details
        print(f"User: {data['User_name']}")
        print(f"Date of Birth: {data['date_of_birth']}")
        print(f"Place of Birth: {data['place_of_birth']}")
        
        print("\nDetected Stelliums:\n")
        
        # Print sign stelliums
        if "stelliums" in data and "sign_stelliums" in data["stelliums"]:
            print("Sign Stelliums:")
            for sign, planets in data["stelliums"]["sign_stelliums"].items():
                print(f"  {sign}: {', '.join(planets)} ({len(planets)} planets)")
        
        # Print house stelliums
        if "stelliums" in data and "house_stelliums" in data["stelliums"]:
            print("\nHouse Stelliums:")
            for house, planets in data["stelliums"]["house_stelliums"].items():
                print(f"  House {house}: {', '.join(planets)} ({len(planets)} planets)")
        
        print("\nStellium Descriptions:\n")
        
        # Print stellium descriptions
        if "stelliumDescriptions" in data:
            for stellium in data["stelliumDescriptions"]:
                print(f"{stellium['title']}: {stellium.get('title', 'None')}")
                print(f"Planets: {', '.join(stellium['planets'])} ({stellium['planet_count']} planets)")
                print(f"Traits: {stellium.get('traits', '')}")
                
                # Print a snippet of the description
                description = stellium.get('description', '')
                if description:
                    snippet = description[:100] + "..." if len(description) > 100 else description
                    print(f"Description snippet: {snippet}\n")
        
        # Save the full response to a file
        with open("stellium_response.json", "w") as f:
            json.dump(data, f, indent=2)
        print("Full response saved to stellium_response.json")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    test_stellium_detection() 