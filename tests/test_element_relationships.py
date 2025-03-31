#!/usr/bin/env python
"""
Test script for the element relationship functionality in the natal chart API.
This script sends a request to the API with test birth data and prints the element relationship results.
"""

import requests
import json
from datetime import datetime

def test_element_relationships():
    """
    Test the element relationship functionality by sending a request to the natal chart API
    and printing the element relationship results.
    """
    # API endpoint
    url = "http://localhost:8000/natal-chart/"
    
    # Test data - using a birth chart with a good mix of elements
    data = {
        "name": "Element Relationship Test User",
        "date_of_birth": "1990-05-15",  # A date with a good mix of elements
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
            with open("element_relationships_response.json", "w") as f:
                json.dump(result, f, indent=2)
                
            print("\n=== Element Relationship Test Results ===")
            print(f"User: {result.get('User_name')}")
            print(f"Birth Date: {result.get('date_of_birth')}")
            print(f"Birth Time: {result.get('time_of_birth', 'Not provided')}")
            print(f"Birth Place: {result.get('place_of_birth')}")
            
            # Print element percentages for reference
            element_analysis = result.get("elementAnalysis", {})
            if element_analysis:
                print("\n=== Element Percentages ===")
                percentages = element_analysis.get("percentages", {})
                for element, percentage in percentages.items():
                    print(f"{element}: {percentage:.1f}%")
            
            # Print primary element relationship
            primary_relationship = result.get("elementRelationship", {})
            if primary_relationship:
                print("\n=== Primary Element Relationship ===")
                print(f"Primary Element: {primary_relationship.get('primary_element')} ({primary_relationship.get('primary_percentage', 0):.1f}%)")
                print(f"Secondary Element: {primary_relationship.get('secondary_element')} ({primary_relationship.get('secondary_percentage', 0):.1f}%)")
                
                relationship = primary_relationship.get("relationship", {})
                print(f"\nTitle: {relationship.get('title', 'Unknown')}")
                print(f"Description: {relationship.get('description', 'No description available')}")
                
                print("\nStrengths:")
                for strength in relationship.get("strengths", []):
                    print(f"- {strength}")
                    
                print("\nChallenges:")
                for challenge in relationship.get("challenges", []):
                    print(f"- {challenge}")
                    
                print("\nIntegration Strategies:")
                for strategy in relationship.get("integration_strategies", []):
                    print(f"- {strategy}")
                    
                print(f"\nPsychological Insight: {relationship.get('psychological_insight', 'None')}")
            else:
                print("\nNo primary element relationship found in the response.")
            
            # Print all element relationships
            all_relationships = result.get("allElementRelationships", [])
            if all_relationships:
                print("\n=== All Element Relationships ===")
                for i, rel in enumerate(all_relationships, 1):
                    elements = rel.get("elements", [])
                    percentages = rel.get("percentages", [])
                    relationship = rel.get("relationship", {})
                    
                    print(f"\nRelationship {i}: {elements[0]}-{elements[1]}")
                    print(f"{elements[0]}: {percentages[0]:.1f}%, {elements[1]}: {percentages[1]:.1f}%")
                    print(f"Title: {relationship.get('title', 'Unknown')}")
                    print(f"Description: {relationship.get('description', 'No description available')[:100]}...")
            else:
                print("\nNo element relationships found in the response.")
            
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
            
    except Exception as e:
        print(f"Exception occurred: {e}")

if __name__ == "__main__":
    test_element_relationships() 