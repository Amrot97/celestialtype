# CelestialType API Response Structure

This document outlines the structure of the CelestialType API responses for reference.

## Main Natal Chart Endpoint

`POST /natal-chart/`

### Request Format

```json
{
  "name": "User Name",
  "date_of_birth": "YYYY-MM-DD",
  "time_of_birth": "HH:MM:SS",  // Optional
  "place_of_birth": "City, Country"
}
```

### Response Structure

The response includes the following main sections:

```json
{
  "User_name": "string",
  "date_of_birth": "string",
  "place_of_birth": "string",
  "coordinates": {
    "latitude": float,
    "longitude": float
  },
  "has_time": boolean,
  "overview": {...},                // Overview data for the app's Overview tab
  "psychologicalInsights": [...],  // Array of insights
  "stelliumDescriptions": [...],   // Array of stellium descriptions
  "modalityAnalysis": {...},       // Modality distribution analysis
  "elements_tab": {...},          // Consolidated element analysis for UI
  "patterns_tab": {...},          // Consolidated patterns (modality and stelliums) for UI
  "allElementRelationships": [...]  // All significant element relationships
}
```

## Overview Tab Structure

Consolidated summary data for the Overview tab:

```json
{
  "basic_info": {
    "name": "string",
    "sun_sign": "string",
    "date_of_birth": "string",
    "place_of_birth": {
      "name": "string",
      "coordinates": {
        "latitude": float,
        "longitude": float
      }
    }
  },
  "cosmic_profile": {
    "elemental_balance": {
      "distribution": [
        {
          "name": "Fire",
          "value": integer
        },
        {
          "name": "Earth",
          "value": integer
        },
        {
          "name": "Air",
          "value": integer
        },
        {
          "name": "Water",
          "value": integer
        }
      ],
      "dominant_elements": ["element1", "element2"],
      "description": "Description of elemental balance"
    },
    "modality_balance": [
      {
        "name": "Cardinal",
        "value": integer
      },
      {
        "name": "Fixed",
        "value": integer
      },
      {
        "name": "Mutable",
        "value": integer
      }
    ],
    "dominant_planets": [
      {
        "name": "Sun",
        "value": integer
      },
      {
        "name": "Moon",
        "value": integer
      },
      {
        "name": "Venus",
        "value": integer
      }
    ]
  },
  "key_insights": {
    "sun": {
      "sign": "string",
      "title": "Core Identity",
      "description": "Description of Sun's influence"
    },
    "moon": {
      "sign": "string",
      "title": "Emotions",
      "description": "Description of Moon's influence"
    },
    "venus": {
      "sign": "string",
      "title": "Values & Love",
      "description": "Description of Venus's influence"
    },
    "mars": {
      "sign": "string",
      "title": "Action & Drive",
      "description": "Description of Mars's influence"
    }
  },
  "stellium": {
    "has_stellium": boolean,
    "title": "string",
    "subtitle": "string",
    "description": "string"
  }
}
```

## Psychological Insights

Array of objects, each representing a psychological insight for a planet:

```json
{
  "title": "Planet in Sign",
  "traits": "Comma-separated list of traits",
  "explanation": "General explanation of the placement",
  
  // Sun insights include:
  "innate_talents": "Description of talents",
  "growth_areas": "Description of growth areas",
  "personal_growth": "Advice for personal growth",
  "closing_affirmation": "Affirmation statement",
  
  // Moon insights include:
  "emotional_strengths": "Description of emotional strengths",
  "emotional_challenges": "Description of emotional challenges",
  "actionable_emotional_care": "Self-care advice",
  "closing_affirmation": "Affirmation statement",
  
  // Venus/Mars insights include:
  "strengths_in_connection": "Relationship strengths",
  "challenges_to_refine": "Relationship challenges",
  "actionable_strategies": "Practical strategies",
  "affirmation": "Affirmation statement",
  
  // Outer planets include:
  "core_themes": "Main themes of the generational placement",
  "collective_purpose": "Description of generation's purpose",
  "strengths": "Collective strengths",
  "challenges": "Collective challenges",
  "actionable_contribution": "How to contribute",
  "affirmation": "Affirmation statement"
}
```

## Stellium Descriptions

Array of objects describing stelliums (concentrations of planets):

```json
{
  "planets": ["Planet1", "Planet2", "Planet3", ...],
  "title": "X Planets in Sign",
  "subtitle": "Type of Stellium",
  "text": "Detailed description of the stellium's effect"
}
```

## Modality Analysis

Analysis of Cardinal, Fixed, and Mutable energies:

```json
{
  "dominant_modality": "cardinal|fixed|mutable",
  "percentages": {
    "cardinal": integer,
    "fixed": integer,
    "mutable": integer
  },
  "modality_percentages": [
    {
      "name": "cardinal|fixed|mutable",
      "value": integer
    },
    // Sorted by value in descending order
  ],
  "description": {
    "dominant": "One sentence summary of dominant modality",
    "cardinal": "Description of cardinal energy expression",
    "fixed": "Description of fixed energy expression",
    "mutable": "Description of mutable energy expression",
    "overall": "Overall modality balance description",
    
    // Detailed dominant modality information
    "dominant_title": "Modality Name (Sign List)",
    "dominant_core_traits": "Key traits of the modality",
    "dominant_description": "Detailed description of modality expression",
    "dominant_strengths": ["Strength1", "Strength2", ...],
    "dominant_challenges": ["Challenge1", "Challenge2", ...],
    "dominant_career_insights": "Career guidance based on modality",
    "dominant_relationship_insights": "Relationship dynamics based on modality",
    "dominant_balance_strategies": ["Strategy1", "Strategy2", ...],
    "dominant_examples": ["Example1", "Example2", ...],
    
    // Overall pattern analysis
    "pattern_summary": "Summary of modality pattern",
    "pattern_life_approach": "How this modality pattern affects life approach",
    "pattern_practical_advice": "Practical advice for this modality pattern"
  }
}
```

## Elements Tab Structure

Comprehensive element analysis data for UI rendering:

```json
{
  "distribution": {
    "fire": integer,
    "earth": integer,
    "air": integer,
    "water": integer,
    "element_percentages": [
      {
        "name": "fire|earth|air|water",
        "value": integer
      },
      // Sorted by value in descending order
    ],
    "dominant_elements": ["element1", "element2"],
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
    "personal_planets": {
      "fire": integer,
      "earth": integer,
      "air": integer,
      "water": integer
    },
    "transpersonal_planets": {
      "fire": integer,
      "earth": integer,
      "air": integer,
      "water": integer
    },
    "interpretation": "Analysis of conscious and unconscious elemental patterns"
  }
}
```

## Patterns Tab Structure

Consolidated patterns data combining modality analysis and stellium information:

```json
{
  "modality": {
    "has_dominant_modality": boolean,
    "dominant_modality": "cardinal|fixed|mutable",
    "distribution": [
      {
        "name": "cardinal|fixed|mutable",
        "value": integer
      },
      // Sorted by value in descending order
    ],
    "title": "Modality Name (Sign List)",
    "core_traits": "Key traits of the modality",
    "summary": "Overall description of modality pattern",
    "detailed_description": "Detailed description of modality expression",
    "strengths": ["Strength1", "Strength2", ...],
    "challenges": ["Challenge1", "Challenge2", ...],
    "practical_advice": "Practical advice for this modality pattern",
    "life_approach": "How this modality pattern affects life approach",
    "career_insights": "Career guidance based on modality",
    "relationship_insights": "Relationship dynamics based on modality",
    "balance_strategies": ["Strategy1", "Strategy2", ...]
  },
  "stellium": {
    "has_stellium": boolean,
    "count": integer,
    "stelliums": [
      {
        "planets": ["Planet1", "Planet2", "Planet3", ...],
        "title": "X Planets in Sign",
        "subtitle": "Type of Stellium",
        "description": "Detailed description of the stellium's effect"
      },
      // Additional stelliums if present
    ]
  }
}
```

## All Element Relationships

Array of significant element relationships:

```json
[
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
```

## Endpoint-Specific Responses

### Element Analysis Endpoint

`POST /natal-chart/elements/`

Returns the element analysis with both the traditional percentages object and the new element_percentages array format.

```json
{
  "counts": {
    "fire": float,
    "earth": float,
    "air": float,
    "water": float
  },
  "percentages": {
    "fire": integer,
    "earth": integer,
    "air": integer,
    "water": integer
  },
  "element_percentages": [
    {
      "name": "fire|earth|air|water",
      "value": integer
    },
    // Sorted by value in descending order
  ],
  "dominant_element": "fire|earth|air|water",
  "weakest_element": "fire|earth|air|water",
  "element_balance": {
    "fire_earth": "string",
    "air_water": "string"
  },
  "description": {
    // Descriptions of element expressions
  }
}
```

### Element Relationships Endpoint

`POST /natal-chart/elements/relationships/`

Returns element relationship data.

### Modality Analysis Endpoint

`POST /natal-chart/modalities/`

Returns the modality analysis with both the traditional percentages object and the new modality_percentages array format.

```json
{
  "dominant_modality": "cardinal|fixed|mutable",
  "percentages": {
    "cardinal": integer,
    "fixed": integer,
    "mutable": integer
  },
  "modality_percentages": [
    {
      "name": "cardinal|fixed|mutable",
      "value": integer
    },
    // Sorted by value in descending order
  ],
  "description": {
    // Detailed modality descriptions
  }
}
```

### Stellium Detection Endpoint

`POST /natal-chart/stelliums/`

Returns just the stellium descriptions section from the main response.

### Patterns Tab Endpoint

`POST /natal-chart/patterns/`

Returns consolidated patterns data combining modality analysis and stellium information, structured for the Patterns tab UI. 