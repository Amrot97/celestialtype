#!/usr/bin/env python
"""
Test script for the conscious vs. unconscious element analysis feature.

This script sends a request to the natal chart API and verifies that the
conscious vs. unconscious element analysis is working correctly.
"""

import requests
import json
import datetime
import sys

def test_conscious_unconscious_elements():
    """
    Test the conscious vs. unconscious element analysis feature.
    """
    # Define the test data with correct parameter names
    test_data = {
        "name": "Conscious-Unconscious Test User",
        "date_of_birth": "1990-08-15",  # Leo Sun, multiple retrograde planets
        "time_of_birth": "12:00:00",
        "place_of_birth": "New York, USA",
        "include_minor_aspects": True,
        "include_asteroids": True
    }
    
    # Send the request to the API
    url = "http://localhost:8000/natal-chart/"
    print(f"Sending request to {url} with test data:")
    print(json.dumps(test_data, indent=2))
    
    try:
        response = requests.post(url, json=test_data)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Save the response to a file for reference
            with open("conscious_unconscious_test_response.json", "w") as f:
                json.dump(response.json(), f, indent=2)
                
            print(f"\nResponse saved to conscious_unconscious_test_response.json")
            
            # Extract the element analysis from the response
            data = response.json()
            element_analysis = data.get("elementAnalysis", {})
            
            # Check if the conscious_unconscious_analysis is present
            conscious_unconscious_analysis = element_analysis.get("conscious_unconscious_analysis", {})
            if not conscious_unconscious_analysis:
                print("\nERROR: conscious_unconscious_analysis not found in the response")
                return
                
            # Print the educational content
            educational_content = conscious_unconscious_analysis.get("educational_content", {})
            print("\n=== Educational Content ===")
            print(f"Title: {educational_content.get('title')}")
            print(f"Description: {educational_content.get('description')[:100]}...")
            print(f"Personal Planets: {educational_content.get('personal_planets')}")
            print(f"Social Planets: {educational_content.get('social_planets')}")
            print(f"Transpersonal Planets: {educational_content.get('transpersonal_planets')}")
            
            # Print the conscious elements
            conscious_elements = conscious_unconscious_analysis.get("conscious_elements", {})
            print("\n=== Conscious Elements (Personal Planets) ===")
            print(f"Description: {conscious_elements.get('description')}")
            print("Percentages:")
            for element, percentage in conscious_elements.get("percentages", {}).items():
                print(f"  {element}: {percentage:.1f}%")
            
            # Print the bridging elements
            bridging_elements = conscious_unconscious_analysis.get("bridging_elements", {})
            print("\n=== Bridging Elements (Social Planets) ===")
            print(f"Description: {bridging_elements.get('description')}")
            print("Percentages:")
            for element, percentage in bridging_elements.get("percentages", {}).items():
                print(f"  {element}: {percentage:.1f}%")
            
            # Print the unconscious elements
            unconscious_elements = conscious_unconscious_analysis.get("unconscious_elements", {})
            print("\n=== Unconscious Elements (Transpersonal Planets) ===")
            print(f"Description: {unconscious_elements.get('description')}")
            print("Percentages:")
            for element, percentage in unconscious_elements.get("percentages", {}).items():
                print(f"  {element}: {percentage:.1f}%")
            
            # Print the significant differences
            significant_differences = conscious_unconscious_analysis.get("significant_differences", {})
            print("\n=== Significant Differences ===")
            if significant_differences:
                for element, data in significant_differences.items():
                    print(f"\nElement: {element}")
                    print(f"Conscious: {data.get('conscious', 0):.1f}%")
                    print(f"Unconscious: {data.get('unconscious', 0):.1f}%")
                    print(f"Difference: {data.get('difference', 0):.1f}%")
                    print(f"Interpretation: {data.get('interpretation')}")
            else:
                print("No significant differences found between conscious and unconscious elements.")
            
            # Compare with overall element percentages
            overall_percentages = element_analysis.get("percentages", {})
            print("\n=== Comparison with Overall Element Percentages ===")
            print("Overall percentages:")
            for element, percentage in overall_percentages.items():
                print(f"  {element}: {percentage:.1f}%")
                
            print("\nConscious percentages (Personal Planets):")
            for element, percentage in conscious_elements.get("percentages", {}).items():
                print(f"  {element}: {percentage:.1f}%")
                
            print("\nUnconscious percentages (Transpersonal Planets):")
            for element, percentage in unconscious_elements.get("percentages", {}).items():
                print(f"  {element}: {percentage:.1f}%")
            
            print("\nTest completed successfully!")
            
        else:
            print(f"\nError: {response.status_code}")
            print(response.text)
            
    except Exception as e:
        print(f"\nException occurred: {e}")
        
if __name__ == "__main__":
    print("Starting test for conscious vs. unconscious element analysis...")
    test_conscious_unconscious_elements() 