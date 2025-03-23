#!/usr/bin/env python
"""
Test script for corner cases in the natal chart API.
This script tests enhanced features for element analysis, modality analysis, and stellium detection.
"""

import requests
import json
from datetime import datetime

def test_corner_cases():
    """
    Test the enhanced features for element analysis, modality analysis, and stellium detection.
    """
    # API endpoint
    url = "http://localhost:8000/natal-chart/"
    
    # Test data - using a birth chart with interesting corner cases
    # This date should have multiple retrograde planets and some tight conjunctions
    data = {
        "name": "Corner Case Test User",
        "date_of_birth": "1990-08-15",  # Mercury, Jupiter, Saturn, Uranus, Neptune, Pluto retrograde
        "time_of_birth": "12:00:00",    # Noon
        "place_of_birth": "New York, USA"
    }
    
    # Headers for the request
    headers = {
        "Content-Type": "application/json",
        "X-Requested-With": "XMLHttpRequest"  # For CSRF exemption in Django
    }
    
    print(f"Sending request to {url} with data: {data}")
    
    try:
        # Send the request
        response = requests.post(url, json=data, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the response
            result = response.json()
            
            # Save the full response to a file for reference
            with open("corner_cases_response.json", "w") as f:
                json.dump(result, f, indent=2)
                
            print("\n=== Corner Cases Test Results ===")
            print(f"User: {result.get('User_name')}")
            print(f"Birth Date: {result.get('date_of_birth')}")
            print(f"Birth Time: {result.get('time_of_birth', 'Not provided')}")
            print(f"Birth Place: {result.get('place_of_birth')}")
            
            # Test Element Analysis Corner Cases
            test_element_analysis_corner_cases(result)
            
            # Test Modality Analysis Corner Cases
            test_modality_analysis_corner_cases(result)
            
            # Test Stellium Detection Corner Cases
            test_stellium_detection_corner_cases(result)
            
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
            
    except Exception as e:
        print(f"Exception occurred: {e}")

def test_element_analysis_corner_cases(result):
    """Test element analysis corner cases."""
    print("\n=== Element Analysis Corner Cases ===")
    
    element_analysis = result.get("elementAnalysis", {})
    if not element_analysis:
        print("No element analysis found in the response.")
        return
    
    # Check for absent elements
    absent_elements = element_analysis.get("absent_elements", [])
    if absent_elements:
        print("\nAbsent Elements:")
        for element in absent_elements:
            print(f"- {element}")
    else:
        print("\nNo completely absent elements found.")
    
    # Check for retrograde planets
    retrograde_planets = element_analysis.get("retrograde_planets", [])
    if retrograde_planets:
        print("\nRetrograde Planets:")
        for planet in retrograde_planets:
            print(f"- {planet}")
    else:
        print("\nNo retrograde planets found.")
    
    # Check for personal planets analysis
    personal_planets_analysis = element_analysis.get("personal_planets_analysis", {})
    if personal_planets_analysis:
        print("\nPersonal Planets Analysis:")
        percentages = personal_planets_analysis.get("percentages", {})
        for element, percentage in percentages.items():
            print(f"- {element}: {percentage:.1f}%")
        
        absent_personal = personal_planets_analysis.get("absent_elements", [])
        if absent_personal:
            print("\nAbsent Elements in Personal Planets:")
            for element in absent_personal:
                print(f"- {element}")
    else:
        print("\nNo personal planets analysis found.")

def test_modality_analysis_corner_cases(result):
    """Test modality analysis corner cases."""
    print("\n=== Modality Analysis Corner Cases ===")
    
    modality_analysis = result.get("modalityAnalysis", {})
    if not modality_analysis:
        print("No modality analysis found in the response.")
        return
    
    # Check for special cases
    special_cases = modality_analysis.get("special_cases", {})
    if special_cases:
        # Check for absent modalities
        absent_modalities = special_cases.get("absent_modalities", [])
        if absent_modalities:
            print("\nAbsent Modalities:")
            for modality in absent_modalities:
                print(f"- {modality}")
        else:
            print("\nNo completely absent modalities found.")
        
        # Check for retrograde planets
        retrograde_planets = special_cases.get("retrograde_planets", [])
        if retrograde_planets:
            print("\nRetrograde Planets (Modality Analysis):")
            for planet in retrograde_planets:
                print(f"- {planet}")
        else:
            print("\nNo retrograde planets found in modality analysis.")
        
        # Check for planets at critical degrees
        critical_degree_planets = special_cases.get("critical_degree_planets", [])
        if critical_degree_planets:
            print("\nPlanets at Critical Degrees:")
            for planet in critical_degree_planets:
                print(f"- {planet}")
        else:
            print("\nNo planets at critical degrees found.")
    else:
        print("\nNo special cases found in modality analysis.")

def test_stellium_detection_corner_cases(result):
    """Test stellium detection corner cases."""
    print("\n=== Stellium Detection Corner Cases ===")
    
    stelliums = result.get("stelliums", {})
    if not stelliums:
        print("No stelliums found in the response.")
        return
    
    # Check for tight stelliums
    sign_stelliums = stelliums.get("sign_stelliums", {})
    tight_sign_stelliums = {k: v for k, v in sign_stelliums.items() if "(Tight Cluster" in k}
    if tight_sign_stelliums:
        print("\nTight Sign Stelliums:")
        for sign, planets in tight_sign_stelliums.items():
            print(f"- {sign}: {', '.join(planets)}")
    else:
        print("\nNo tight sign stelliums found.")
    
    # Check for stellium strength
    sign_stellium_strength = stelliums.get("sign_stellium_strength", {})
    if sign_stellium_strength:
        print("\nStellium Strength:")
        for sign, strength in sign_stellium_strength.items():
            print(f"- {sign}: {strength.get('classification', 'Unknown')} (Score: {strength.get('score', 0)})")
    else:
        print("\nNo stellium strength information found.")
    
    # Check for house stelliums
    house_stelliums = stelliums.get("house_stelliums", {})
    if house_stelliums:
        print("\nHouse Stelliums:")
        for house, planets in house_stelliums.items():
            print(f"- House {house}: {', '.join(planets)}")
    else:
        print("\nNo house stelliums found.")

if __name__ == "__main__":
    test_corner_cases() 