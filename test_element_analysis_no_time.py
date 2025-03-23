#!/usr/bin/env python
"""
Test script for the element analysis functionality in the natal chart API without birth time.
This script sends a request to the API with test birth data (no time) and prints the element analysis results.
"""

import requests
import json
from datetime import datetime

def test_element_analysis_no_time():
    """
    Test the element analysis functionality by sending a request to the natal chart API
    without birth time and printing the element analysis results.
    """
    # API endpoint
    url = "http://localhost:8000/natal-chart/"
    
    # Test data - using a birth chart with a good mix of elements, but no time
    data = {
        "name": "Element Test User (No Time)",
        "date_of_birth": "1990-05-15",  # A date with a good mix of elements
        "place_of_birth": "New York, USA"
        # No time_of_birth provided
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
            with open("element_analysis_no_time_response.json", "w") as f:
                json.dump(result, f, indent=2)
                
            print("\n=== Element Analysis Test Results (No Time) ===")
            print(f"User: {result.get('User_name')}")
            print(f"Birth Date: {result.get('date_of_birth')}")
            print(f"Birth Time: {result.get('time_of_birth', 'Not provided')}")
            print(f"Birth Place: {result.get('place_of_birth')}")
            print(f"Has Time: {result.get('has_time', False)}")
            
            # Print element analysis information
            element_analysis = result.get("elementAnalysis", {})
            
            if element_analysis:
                print("\n=== Element Percentages ===")
                percentages = element_analysis.get("percentages", {})
                for element, percentage in percentages.items():
                    print(f"{element}: {percentage:.1f}%")
                
                print("\n=== Planets by Element ===")
                planets_by_element = element_analysis.get("planets_by_element", {})
                for element, planets in planets_by_element.items():
                    print(f"{element}: {', '.join(planets)}")
                
                print("\n=== Element Balance Analysis ===")
                balance_analysis = element_analysis.get("balance_analysis", {})
                
                # Print pattern information
                pattern = balance_analysis.get("pattern", {})
                if pattern:
                    print(f"Pattern: {pattern.get('title', 'Unknown')}")
                    print(f"Description: {pattern.get('description', 'No description available')}")
                    
                    print("\nStrengths:")
                    for strength in pattern.get("strengths", []):
                        print(f"- {strength}")
                        
                    print("\nDevelopment Areas:")
                    for area in pattern.get("development_areas", []):
                        print(f"- {area}")
                
                # Print dominant elements
                dominant_elements = balance_analysis.get("dominant_elements", [])
                if dominant_elements:
                    print("\nDominant Elements:")
                    for element in dominant_elements:
                        print(f"\n- {element.get('title', 'Unknown')}")
                        print(f"  Level: {element.get('level', 'high')}")
                        print(f"  Core Traits: {element.get('core_traits', 'None')}")
                        print(f"  Description: {element.get('description', 'No description available')}")
                        print(f"  High Description: {element.get('high_description', 'No description available')}")
                        
                        print("\n  High Strengths:")
                        for strength in element.get("high_strengths", []):
                            print(f"  - {strength}")
                            
                        print("\n  High Challenges:")
                        for challenge in element.get("high_challenges", []):
                            print(f"  - {challenge}")
                
                # Print moderate elements
                moderate_elements = balance_analysis.get("moderate_elements", [])
                if moderate_elements:
                    print("\nModerate Elements:")
                    for element in moderate_elements:
                        print(f"\n- {element.get('title', 'Unknown')}")
                        print(f"  Level: {element.get('level', 'moderate')}")
                        print(f"  Core Traits: {element.get('core_traits', 'None')}")
                        print(f"  Description: {element.get('description', 'No description available')}")
                        
                        # For moderate elements, we include both high and low descriptions
                        print(f"  Balanced Description: {element.get('high_description', 'No description available')}")
                        
                        print("\n  Strengths:")
                        for strength in element.get("high_strengths", []):
                            print(f"  - {strength}")
                            
                        print("\n  Potential Challenges:")
                        for challenge in element.get("high_challenges", []):
                            print(f"  - {challenge}")
                
                # Print lacking elements
                lacking_elements = balance_analysis.get("lacking_elements", [])
                if lacking_elements:
                    print("\nLacking Elements:")
                    for element in lacking_elements:
                        print(f"\n- {element.get('title', 'Unknown')}")
                        print(f"  Level: {element.get('level', 'low')}")
                        print(f"  Core Traits: {element.get('core_traits', 'None')}")
                        print(f"  Description: {element.get('description', 'No description available')}")
                        print(f"  Low Description: {element.get('low_description', 'No description available')}")
                        
                        print("\n  Low Challenges:")
                        for challenge in element.get("low_challenges", []):
                            print(f"  - {challenge}")
                            
                        print("\n  Development Strategies:")
                        for strategy in element.get("development_strategies", []):
                            print(f"  - {strategy}")
            else:
                print("No element analysis data found in the response.")
            
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
            
    except Exception as e:
        print(f"Exception occurred: {e}")

if __name__ == "__main__":
    test_element_analysis_no_time() 