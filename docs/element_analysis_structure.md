# Element Analysis Structure

This document details the structure and implementation approach for the Element Analysis component of the CelestialType API.

## Overview

The `elements_tab` object in the API response provides comprehensive analysis of the elemental distribution in a natal chart, including element relationships and their psychological significance.

## Response Structure

```json
{
  "distribution": {
    "Fire": integer,
    "Earth": integer,
    "Air": integer,
    "Water": integer,
    "element_percentages": [
      {
        "name": "Fire|Earth|Air|Water",
        "value": integer
      },
      // Sorted by value in descending order
    ],
    "dominant_elements": ["Element1", "Element2"], // Capitalized element names
    "title": "Your Element Balance: Element-Element Emphasis",
    "description": "Description of elemental balance meaning"
  },
  "relationship": {
    "primary_relationship": "element1-element2",
    "title": "Element Relationship: Element1-Element2",
    "subtitle": "Element1-Element2 Relationship: Descriptive Title",
    "description": "Description of how these elements interact",
    "strengths": [
      "Strength1",
      "Strength2",
      "Strength3",
      "Strength4",
      "Strength5"
    ],
    "integration_strategies": [
      "Strategy1",
      "Strategy2",
      "Strategy3",
      "Strategy4",
      "Strategy5"
    ]
  },
  "conscious_vs_unconscious": {
    "personal_planets": [
      {
        "name": "Fire|Earth|Air|Water",
        "value": integer
      },
      // Additional elements
    ],
    "transpersonal_planets": [
      {
        "name": "Fire|Earth|Air|Water",
        "value": integer
      },
      // Additional elements
    ],
    "interpretation": "Analysis of conscious and unconscious elemental patterns"
  },
  "allElementRelationships": [
    {
      "element1": "fire|earth|air|water",
      "element2": "fire|earth|air|water",
      "element1_percentage": integer,
      "element2_percentage": integer,
      "interaction": "Type of interaction",
      "harmony": "harmonious|complex|challenging",
      "description": "Description of the relationship",
      "balance": "Description of balance state",
      "significance": float
    },
    // Additional relationships...
  ]
}
```

## Implementation Components

### 1. Element Distribution Analysis

This component calculates the distribution of elements in the chart:

1. **Raw Element Counts**
   - Count planets in each element (Fire, Earth, Air, Water)
   - Store raw counts in the distribution object

2. **Percentage Calculation**
   - Convert raw counts to percentages
   - Format as sorted array of name-value objects

3. **Dominant Element Detection**
   - Apply threshold logic to identify dominant elements
   - Consider both absolute count and relative proportion
   - Store as array of capitalized element names

4. **Title Generation**
   - Create a descriptive title based on dominant elements
   - Format: "Your Element Balance: Element-Element Emphasis"

5. **Description Generation**
   - Generate meaningful description of the elemental balance
   - Highlight psychological implications of the distribution

### 2. Element Relationship Analysis

This component analyzes the relationship between the most significant elements:

1. **Primary Relationship Identification**
   - Identify the two most significant elements
   - Format as "element1-element2" (lowercase)

2. **Title and Subtitle Generation**
   - Create title: "Element Relationship: Element1-Element2"
   - Create subtitle describing the nature of the relationship

3. **Relationship Description**
   - Generate detailed description of how these elements interact
   - Explain psychological implications of this combination

4. **Strengths Identification**
   - List 5 key strengths of this elemental combination
   - Focus on positive synergies and complementary aspects

5. **Integration Strategies**
   - Provide 5 practical strategies for integrating these elements
   - Focus on actionable advice for personal development

### 3. Conscious vs. Unconscious Elements

This component contrasts the elemental distribution between personal and transpersonal planets:

1. **Planet Classification**
   - Group planets as personal (Sun through Mars) or transpersonal (Jupiter through Pluto)
   - Calculate elemental distribution for each group

2. **Distribution Formatting**
   - Format distributions as arrays of name-value objects
   - Sort by value in descending order

3. **Interpretation Generation**
   - Compare and contrast the two distributions
   - Generate psychological interpretation of the differences
   - Focus on conscious awareness vs. unconscious patterns

### 4. Complete Element Relationship Matrix

This component provides a comprehensive analysis of all possible element pairs:

1. **Relationship Pair Generation**
   - Generate all possible element pairs (10 total)
   - Calculate significance based on element percentages

2. **Interaction Analysis**
   - Determine interaction type for each pair
   - Classify harmony as harmonious, complex, or challenging

3. **Description and Balance**
   - Generate description of each relationship
   - Assess balance state between the elements

4. **Significance Calculation**
   - Calculate significance score for each relationship
   - Consider element percentages and interaction type

## Implementation Approach

### Element Distribution Calculation

```python
def calculate_element_distribution(planet_positions):
    """Calculate the distribution of elements in the chart."""
    # Initialize counters
    elements = {"Fire": 0, "Earth": 0, "Air": 0, "Water": 0}
    
    # Count elements for each planet
    for planet in planet_positions:
        element = planet["sign"]["element"].capitalize()
        if element in elements:
            # Apply weighting based on planet type
            weight = get_planet_weight(planet["planet"])
            elements[element] += weight
    
    # Calculate total weight
    total_weight = sum(elements.values())
    
    # Calculate percentages
    percentages = {}
    for element, count in elements.items():
        if total_weight > 0:
            percentages[element] = round((count / total_weight) * 100)
        else:
            percentages[element] = 0
    
    # Create sorted array of percentages
    element_percentages = [
        {"name": element, "value": value}
        for element, value in percentages.items()
    ]
    element_percentages.sort(key=lambda x: x["value"], reverse=True)
    
    # Determine dominant elements (those above 30% or the top two if none above 30%)
    dominant_elements = []
    for element in element_percentages:
        if element["value"] >= 30:
            dominant_elements.append(element["name"])
    
    # If no elements above threshold, take top two
    if not dominant_elements and len(element_percentages) >= 2:
        dominant_elements = [element_percentages[0]["name"], element_percentages[1]["name"]]
    elif not dominant_elements and len(element_percentages) == 1:
        dominant_elements = [element_percentages[0]["name"]]
    
    # Generate title and description
    title = generate_element_balance_title(dominant_elements)
    description = generate_element_balance_description(dominant_elements, percentages)
    
    # Return complete distribution object
    return {
        "Fire": elements["Fire"],
        "Earth": elements["Earth"],
        "Air": elements["Air"],
        "Water": elements["Water"],
        "element_percentages": element_percentages,
        "dominant_elements": dominant_elements,
        "title": title,
        "description": description
    }
```

### Element Relationship Analysis

```python
def analyze_primary_element_relationship(distribution):
    """Analyze the relationship between the two most dominant elements."""
    # Get the two most dominant elements
    dominant_elements = distribution.get("dominant_elements", [])
    
    if len(dominant_elements) < 2:
        # Handle case with fewer than 2 dominant elements
        # Either use the single dominant element with the next highest,
        # or the two highest if no dominants
        percentages = distribution.get("element_percentages", [])
        if len(percentages) >= 2:
            if len(dominant_elements) == 1:
                # Use dominant + next highest
                element1 = dominant_elements[0]
                # Find next highest that's not already in dominant_elements
                for element in percentages:
                    if element["name"] not in dominant_elements:
                        element2 = element["name"]
                        break
            else:
                # Use two highest
                element1 = percentages[0]["name"]
                element2 = percentages[1]["name"]
        else:
            # Not enough elements to analyze
            return None
    else:
        # Use the two dominant elements
        element1 = dominant_elements[0]
        element2 = dominant_elements[1]
    
    # Ensure consistent ordering (alphabetical)
    if element1.lower() > element2.lower():
        element1, element2 = element2, element1
    
    # Get relationship data from templates
    relationship_key = f"{element1.lower()}-{element2.lower()}"
    relationship_data = get_element_relationship_template(relationship_key)
    
    if not relationship_data:
        return None
    
    # Return formatted relationship data
    return {
        "primary_relationship": relationship_key,
        "title": f"Element Relationship: {element1}-{element2}",
        "subtitle": relationship_data.get("subtitle", f"{element1}-{element2} Relationship"),
        "description": relationship_data.get("description", ""),
        "strengths": relationship_data.get("strengths", []),
        "integration_strategies": relationship_data.get("integration_strategies", [])
    }
```

### Conscious vs. Unconscious Analysis

```python
def analyze_conscious_unconscious_elements(planet_positions):
    """Analyze the elemental distribution in personal vs. transpersonal planets."""
    # Define planet groups
    personal_planets = ["Sun", "Moon", "Mercury", "Venus", "Mars"]
    transpersonal_planets = ["Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
    
    # Initialize counters
    personal_elements = {"Fire": 0, "Earth": 0, "Air": 0, "Water": 0}
    transpersonal_elements = {"Fire": 0, "Earth": 0, "Air": 0, "Water": 0}
    
    # Count elements in each group
    for planet in planet_positions:
        planet_name = planet["planet"]
        element = planet["sign"]["element"].capitalize()
        
        if planet_name in personal_planets:
            personal_elements[element] += 1
        elif planet_name in transpersonal_planets:
            transpersonal_elements[element] += 1
    
    # Convert to percentages and format as arrays
    personal_percentages = format_element_percentages(personal_elements)
    transpersonal_percentages = format_element_percentages(transpersonal_elements)
    
    # Generate interpretation
    interpretation = generate_conscious_unconscious_interpretation(personal_percentages, transpersonal_percentages)
    
    return {
        "personal_planets": personal_percentages,
        "transpersonal_planets": transpersonal_percentages,
        "interpretation": interpretation
    }
```

### Complete Element Relationship Matrix

```python
def get_all_element_relationships(distribution):
    """Generate a complete matrix of all element relationships."""
    elements = ["fire", "earth", "air", "water"]
    relationships = []
    
    # Get element percentages as a dictionary for easier lookup
    element_percentages = {
        item["name"].lower(): item["value"] 
        for item in distribution.get("element_percentages", [])
    }
    
    # Generate all unique pairs
    for i in range(len(elements)):
        for j in range(i+1, len(elements)):
            element1 = elements[i]
            element2 = elements[j]
            
            # Get percentages
            element1_percentage = element_percentages.get(element1, 0)
            element2_percentage = element_percentages.get(element2, 0)
            
            # Skip if both elements have 0%
            if element1_percentage == 0 and element2_percentage == 0:
                continue
            
            # Get relationship data
            relationship_key = f"{element1}-{element2}"
            template = get_element_relationship_template(relationship_key)
            
            # Calculate significance based on combined percentage and relationship type
            combined_percentage = element1_percentage + element2_percentage
            harmony_factor = {
                "harmonious": 1.2,
                "complex": 1.0,
                "challenging": 0.8
            }.get(template.get("harmony", "complex"), 1.0)
            
            significance = round((combined_percentage / 100) * harmony_factor, 2)
            
            # Create relationship object
            relationship = {
                "element1": element1,
                "element2": element2,
                "element1_percentage": element1_percentage,
                "element2_percentage": element2_percentage,
                "interaction": template.get("interaction", "Undefined interaction"),
                "harmony": template.get("harmony", "complex"),
                "description": template.get("description", ""),
                "balance": generate_balance_description(element1_percentage, element2_percentage),
                "significance": significance
            }
            
            relationships.append(relationship)
    
    # Sort by significance
    relationships.sort(key=lambda x: x["significance"], reverse=True)
    
    return relationships
```

## Helper Functions

```python
def get_planet_weight(planet_name):
    """Get the weight/influence of a planet for element calculations."""
    weights = {
        "Sun": 3.0,
        "Moon": 2.5,
        "Mercury": 1.0,
        "Venus": 1.0,
        "Mars": 1.0,
        "Jupiter": 1.0,
        "Saturn": 1.0,
        "Uranus": 0.5,
        "Neptune": 0.5,
        "Pluto": 0.5,
        "Ascendant": 2.0,
        "Midheaven": 1.0
    }
    return weights.get(planet_name, 0.5)

def format_element_percentages(elements):
    """Convert element counts to percentages and format as sorted array."""
    total = sum(elements.values())
    percentages = []
    
    for element, count in elements.items():
        if total > 0:
            value = round((count / total) * 100)
        else:
            value = 0
        
        percentages.append({"name": element, "value": value})
    
    # Sort by value in descending order
    percentages.sort(key=lambda x: x["value"], reverse=True)
    
    return percentages

def generate_element_balance_title(dominant_elements):
    """Generate a title for the element balance section."""
    if not dominant_elements:
        return "Your Element Balance: Balanced Distribution"
    
    if len(dominant_elements) == 1:
        return f"Your Element Balance: {dominant_elements[0]} Emphasis"
    
    return f"Your Element Balance: {dominant_elements[0]}-{dominant_elements[1]} Emphasis"

def generate_element_balance_description(dominant_elements, percentages):
    """Generate a description of the elemental balance."""
    # Implementation would load from templates based on dominant elements
    pass

def get_element_relationship_template(relationship_key):
    """Get the template for a specific element relationship."""
    # Implementation would load from a dictionary of templates
    # Example: ELEMENT_RELATIONSHIPS["fire-water"]
    pass

def generate_conscious_unconscious_interpretation(personal, transpersonal):
    """Generate an interpretation of conscious vs. unconscious elements."""
    # Implementation would compare distributions and generate insight
    pass

def generate_balance_description(percentage1, percentage2):
    """Generate a description of the balance between two elements."""
    difference = abs(percentage1 - percentage2)
    
    if difference < 10:
        return "These elements are in balance, allowing for integration of their qualities."
    elif difference < 20:
        return "These elements are moderately imbalanced, with one slightly more dominant."
    else:
        return "These elements are significantly imbalanced, with one clearly more dominant."
```

## Data Storage

Element relationship templates should be stored in JSON files or Python dictionaries:

```python
ELEMENT_RELATIONSHIPS = {
    "fire-earth": {
        "subtitle": "Fire-Earth Relationship: Creative Manifestation",
        "description": "The Fire-Earth relationship combines inspiration with practicality...",
        "interaction": "Inspiration meets practicality",
        "harmony": "complex",
        "strengths": [
            "Ability to turn ideas into reality",
            "Balanced approach to action and patience",
            "Practical creativity",
            "Persistent drive",
            "Resourceful problem-solving"
        ],
        "integration_strategies": [
            "Set achievable milestones for your inspired ideas",
            "Balance spontaneity with planning",
            "Use earth's patience to sustain fire's enthusiasm",
            "Create tangible expressions of your creative vision",
            "Ground your ambitions in realistic assessment"
        ]
    },
    "fire-air": {
        // Fire-Air relationship data
    },
    // More relationships...
}
```

## Element Analysis Workflow

1. Calculate element distribution from planet positions
2. Identify dominant elements
3. Generate distribution descriptions and titles
4. Analyze primary element relationship
5. Analyze conscious vs. unconscious elements
6. Generate complete relationship matrix
7. Assemble final response structure 