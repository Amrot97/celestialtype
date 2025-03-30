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
  "has_time": boolean,
  "time_of_birth": "string",  // Only included if has_time is true
  "overview": {...},                // Overview data for the app's Overview tab
  "psychologicalInsights": [...],  // Array of insights
  "elements_tab": {...},          // Consolidated element analysis for UI
  "patterns_tab": {...}           // Consolidated patterns (modality and stelliums) for UI
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

## Standalone Endpoints

The API provides several standalone endpoints that return specific parts of the natal chart analysis:

### Elements Tab Endpoint

`POST /natal-chart/elements/`

Returns the same structure as the `elements_tab` field in the main response.

### Patterns Tab Endpoint

`POST /natal-chart/patterns/`

Returns the same structure as the `patterns_tab` field in the main response.

### Element Relationships Endpoint

`POST /natal-chart/elements/relationships/`

Returns element relationship data for detailed analysis of how elements interact in the chart.