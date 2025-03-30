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
  "psychologicalInsights": [...],  // Array of insights
  "stelliumDescriptions": [...],   // Array of stellium descriptions
  "modalityAnalysis": {...},       // Modality distribution analysis
  "elements_tab": {...},          // Consolidated element analysis for UI
  "allElementRelationships": [...]  // All significant element relationships
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

Returns just the element analysis section from the main response.

### Element Relationships Endpoint

`POST /natal-chart/elements/relationships/`

Returns element relationship data.

### Modality Analysis Endpoint

`POST /natal-chart/modalities/`

Returns just the modality analysis section from the main response.

### Stellium Detection Endpoint

`POST /natal-chart/stelliums/`

Returns just the stellium descriptions section from the main response. 