#!/usr/bin/env python
"""
Debug script for the natal chart API endpoint.
"""
import requests
import json
import sys

def debug_natal_chart_api():
    """Debug the natal chart API endpoint with detailed error reporting."""
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
    
    print(f"Sending POST request to {url}")
    print(f"Headers: {json.dumps(headers, indent=2)}")
    print(f"Data: {json.dumps(data, indent=2)}")
    
    try:
        response = requests.post(url, json=data, headers=headers)
        print(f"\nResponse status code: {response.status_code}")
        print(f"Response headers: {json.dumps(dict(response.headers), indent=2)}")
        
        # Try to parse as JSON first
        try:
            result = response.json()
            print("\nJSON Response:")
            print(json.dumps(result, indent=2))
        except json.JSONDecodeError:
            # If not JSON, print the text response
            print("\nText Response (first 1000 characters):")
            print(response.text[:1000])
            print("...")
            
            # Save the full response to a file for inspection
            with open("full_response.html", "w") as f:
                f.write(response.text)
                print("\nFull response saved to full_response.html")
        
        # Check for specific error patterns
        if response.status_code != 200:
            print("\nError Analysis:")
            if "CSRF" in response.text:
                print("- CSRF token issue detected")
            if "Authentication" in response.text or "authentication" in response.text:
                print("- Authentication issue detected")
            if "permission" in response.text or "Permission" in response.text:
                print("- Permission issue detected")
            if "serializer" in response.text or "Serializer" in response.text:
                print("- Serializer validation issue detected")
            
    except requests.RequestException as e:
        print(f"Request Exception: {e}")
        
    except Exception as e:
        print(f"Unexpected Exception: {e}")

if __name__ == "__main__":
    debug_natal_chart_api() 