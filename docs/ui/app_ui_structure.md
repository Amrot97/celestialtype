# CelestialType App UI Structure

This document outlines the structure and content requirements for each subtab of the CelestialType application.

## Overview Tab

The Overview tab provides a high-level summary of the user's astrological profile, including basic information and key insights.

### Structure

1. **Basic Information**
   - User's name
   - Sun sign
   - Date of birth
   - Place of birth with location coordinates

2. **Cosmic Profile Section**
   - Three charts displaying percentages for:
     - Elemental balance (Fire, Earth, Air, Water)
     - Modality balance (Cardinal, Fixed, Mutable)
     - Dominant planets

3. **Elemental Balance Description**
   - Description of the user's dominant elements (e.g., Fire and Earth combination)
   - Interpretation of what this combination means for the user's personality

4. **Key Insights Section**
   - **Sun: Core Identity**
     - Description of the user's Sun sign and its influence on their core identity
   - **Moon: Emotions**
     - Description of the user's Moon sign and its influence on their emotional nature
   - **Venus: Values & Love**
     - Description of the user's Venus placement and its influence on their values and approach to love
   - **Mars: Action & Drive**
     - Description of the user's Mars placement and its influence on their drive and actions

5. **Stellium Section** (conditional)
   - Title: "Your [Sign/House] Stellium"
   - Subtitle indicating the location or nature of the stellium
   - Description explaining the significance and influence of the stellium on the user's life

### API Response Structure for Overview Tab

```json
{
  "overview": {
    "basic_info": {
      "name": "User Name",
      "sun_sign": "Leo",
      "date_of_birth": "1990-08-15",
      "place_of_birth": {
        "name": "New York, USA",
        "coordinates": {
          "latitude": 40.7128,
          "longitude": -74.0060
        }
      }
    },
    "cosmic_profile": {
      "elemental_balance": {
        "fire": 35,
        "earth": 25,
        "air": 20,
        "water": 20,
        "dominant_elements": ["fire", "earth"],
        "description": "Your Fire and Earth combination makes you both passionate and practical. You have the drive to pursue your goals with enthusiasm while maintaining the groundedness to see them through to completion."
      },
      "modality_balance": {
        "cardinal": 40,
        "fixed": 45,
        "mutable": 15,
        "dominant_modality": "fixed",
        "description": "Your dominant Fixed modality gives you persistence and determination. You excel at maintaining focus and seeing projects through to completion, even when faced with obstacles."
      },
      "dominant_planets": {
        "planets": ["Sun", "Mars", "Saturn"],
        "description": "With the Sun, Mars, and Saturn as your dominant planets, you have a strong sense of self, abundant energy to pursue your goals, and the discipline to overcome challenges."
      }
    },
    "key_insights": {
      "sun": {
        "sign": "Leo",
        "title": "Core Identity",
        "description": "With your Sun in Leo, you shine with creativity, confidence, and leadership. You naturally draw attention and have a generous heart. Your purpose involves authentic self-expression and inspiring others through your natural charisma and talents."
      },
      "moon": {
        "sign": "Taurus",
        "title": "Emotions",
        "description": "Your Moon in Taurus creates an emotional nature that seeks stability and comfort. You process feelings slowly and thoroughly, requiring security and consistency in your emotional life. You find peace through connecting with nature and enjoying sensory pleasures."
      },
      "venus": {
        "sign": "Cancer",
        "title": "Values & Love",
        "description": "With Venus in Cancer, you value emotional security and nurturing connections in relationships. You love deeply and protectively, offering unwavering support to those you care about. You're attracted to partners who are emotionally available and family-oriented."
      },
      "mars": {
        "sign": "Scorpio",
        "title": "Action & Drive",
        "description": "Mars in Scorpio gives you intense determination and strategic focus in pursuing your goals. You act with passion and persistence, diving deeply into whatever captures your interest. You have remarkable endurance and the ability to transform difficult situations."
      }
    },
    "stellium": {
      "has_stellium": true,
      "title": "Your Water Sign Stellium",
      "subtitle": "Concentrated in Scorpio",
      "description": "With multiple planets in Scorpio, you have an enhanced connection to your emotional depths and transformative potential. This stellium amplifies your intuition, psychological insight, and ability to navigate complex emotional terrain. You may find yourself drawn to situations that require deep personal transformation and regeneration."
    }
  }
}
```

Note: The actual response will be dynamically generated based on the user's birth chart data. The above example is for illustrative purposes only.

## Elements Tab

The Elements tab provides a detailed analysis of the user's elemental distribution and relationships between elements.

### Structure

1. **Element Distribution**
   - Bar charts showing percentages for each element:
     - Fire
     - Earth
     - Air
     - Water
   - Element Balance title (e.g., "Your Element Balance: Fire-Earth Emphasis")
   - Description of what this elemental combination means for the user

2. **Element Relationship**
   - Title with the specific relationship (e.g., "Element Relationship: Fire-Earth")
   - Subtitle describing the relationship (e.g., "Fire-Earth Relationship: Manifesting Vision")
   - Description of how these elements interact in the user's chart
   - **Strengths** section with bullet points:
     - Transform creative ideas into practical reality
     - Balance vision with methodical implementation
     - Inspire others while delivering concrete results
     - Natural talent for entrepreneurship
     - Sustainable creativity that doesn't burn out quickly
   - **Integration Strategies** section with actionable advice:
     - Create a two-phase approach: visioning (Fire) then implementation (Earth)
     - Practice patience with the manifestation process
     - Use Earth energy to create sustainable structures

3. **Conscious vs. Unconscious Elements**
   - Two side-by-side sections:
     - **Personal Planets (Conscious Experience)**
       - Bar charts showing elemental percentages for personal planets
       - Fire, Earth, Air, Water with percentages
     - **Transpersonal Planets (Unconscious Patterns)**
       - Bar charts showing elemental percentages for transpersonal planets
       - Fire, Earth, Air, Water with percentages
   - **What This Means** section
     - Description explaining the difference between conscious identification and unconscious patterns
     - Interpretation of any disconnects between conscious and unconscious elemental emphasis

### API Response Structure for Elements Tab

```json
{
  "elements": {
    "distribution": {
      "fire": 35,
      "earth": 25,
      "air": 20,
      "water": 20,
      "dominant_elements": ["fire", "earth"],
      "title": "Your Element Balance: Fire-Earth Emphasis",
      "description": "Your chart shows a strong combination of Fire and Earth elements, creating a dynamic balance between inspiration and manifestation. This blend helps you transform creative ideas into practical results while maintaining both enthusiasm and thoroughness."
    },
    "relationship": {
      "primary_relationship": "fire-earth",
      "title": "Element Relationship: Fire-Earth",
      "subtitle": "Fire-Earth Relationship: Manifesting Vision",
      "description": "When Fire and Earth combine in your chart, there's a dynamic tension between inspiration and manifestation. Fire provides the creative spark, enthusiasm, and vision, while Earth offers practicality, patience, and the ability to build tangible results.",
      "strengths": [
        "Transform creative ideas into practical reality",
        "Balance vision with methodical implementation",
        "Inspire others while delivering concrete results",
        "Natural talent for entrepreneurship",
        "Sustainable creativity that doesn't burn out quickly"
      ],
      "integration_strategies": [
        "Create a two-phase approach: visioning (Fire) then implementation (Earth)",
        "Practice patience with the manifestation process",
        "Use Earth energy to create sustainable structures"
      ]
    },
    "conscious_vs_unconscious": {
      "personal_planets": {
        "fire": 35,
        "earth": 25,
        "air": 20,
        "water": 20
      },
      "transpersonal_planets": {
        "fire": 0.0,
        "earth": 53.1,
        "air": 0.0,
        "water": 46.9
      },
      "interpretation": "You consciously identify with Fire qualities (enthusiasm, creativity) and express them readily in your daily life. However, your unconscious patterns are dominated by Earth (practicality) and Water (emotion, intuition). This suggests a disconnect between your conscious self-image and deeper psychological patterns."
    }
  }
}
```

Note: The actual response will be dynamically generated based on the user's birth chart data. The above example is for illustrative purposes only.

## Patterns Tab

The Patterns tab provides insights into the significant astrological patterns in the user's chart, focusing on modality distribution and stellium configurations.

### Structure

1. **Modality Pattern Section**
   - Title with the dominant modality (e.g., "Cardinal Energy (Aries, Cancer, Libra, Capricorn)")
   - Chart showing percentages for modalities:
     - Cardinal
     - Fixed
     - Mutable
   - Core traits of the dominant modality
   - Summary of the modality pattern and its influence
   - **Strengths and Challenges**
     - Two side-by-side sections:
       - Strengths: Bullet points of advantages from this modality pattern
       - Challenges: Bullet points of potential difficulties with this modality pattern
   - **Life Approach**
     - Description of how this modality pattern affects the user's approach to life
   - **Practical Advice**
     - Actionable strategies for leveraging strengths and addressing challenges
   - **Additional Insights** (expandable sections)
     - Career Insights
     - Relationship Insights
     - Balance Strategies

2. **Stellium Section** (conditional)
   - For each stellium:
     - Title (e.g., "4 Planets in Capricorn")
     - Subtitle indicating the type of stellium (e.g., "Tight Sign Stellium")
     - List of planets involved
     - Description explaining the significance and influence of the stellium
   - If multiple stelliums present, each is displayed in its own card or section

### API Response Structure for Patterns Tab

```json
{
  "patterns_tab": {
    "modality": {
      "has_dominant_modality": true,
      "dominant_modality": "Cardinal",
      "distribution": [
        {"name": "Cardinal", "value": 55},
        {"name": "Fixed", "value": 30},
        {"name": "Mutable", "value": 15}
      ],
      "title": "Cardinal Energy (Aries, Cancer, Libra, Capricorn)",
      "core_traits": "Initiative, leadership, action-oriented, pioneering",
      "summary": "Your chart shows a dominance of Cardinal energy (55%), making you naturally oriented toward leadership, initiation, and new beginnings.",
      "detailed_description": "With your strong Cardinal energy, you naturally take charge in situations and excel at launching new projects. You're likely the person who gets things moving in your workplace or social circle. This pioneering spirit makes you an excellent starter and innovator, though you may sometimes leave projects unfinished as you move to the next exciting beginning.",
      "strengths": [
        "Natural leadership abilities that others recognize and respond to",
        "Excellent at crisis management and decisive action",
        "Innovative thinking that leads to new solutions",
        "Ability to motivate others and catalyze group action",
        "Entrepreneurial spirit and comfort with initiating"
      ],
      "challenges": [
        "May start too many projects without completing them",
        "Can become impatient with slower, methodical processes",
        "Might overwhelm others with constant new ideas and initiatives",
        "May struggle with the maintenance phase of projects",
        "Can experience burnout from always being in 'initiation mode'"
      ],
      "practical_advice": "Channel your initiating energy into areas that truly matter to you, and develop systems to ensure follow-through. Consider partnering with people who have complementary Fixed and Mutable strengths to help bring your many initiatives to completion.",
      "life_approach": "You likely approach life as a series of new beginnings and opportunities to lead or pioneer. Your natural inclination is to start projects, initiate conversations, and catalyze change in your environment.",
      "career_insights": "You thrive in roles requiring leadership, crisis management, and innovation. Consider entrepreneurship, emergency services, project initiation roles, leadership positions, or fields requiring quick decision-making. Careers in startups, emergency medicine, sales, leadership consulting, or as a business launcher would leverage your natural strengths.",
      "relationship_insights": "In relationships, you often take the lead in planning activities and resolving issues. Be mindful that partners may sometimes need you to follow their lead or simply maintain comfortable routines. Your decisiveness is valuable, but balance it by developing patience and listening skills.",
      "balance_strategies": [
        "Before starting something new, evaluate your current commitments",
        "Partner with people who have strong Fixed energy to help complete what you start",
        "Schedule regular 'completion days' focused solely on finishing existing projects",
        "Practice mindfulness to become aware of your impulse to start new things",
        "Develop a 'one in, one out' rule: finish or delegate one project before beginning another"
      ]
    },
    "stellium": {
      "has_stellium": true,
      "count": 1,
      "stelliums": [
        {
          "planets": ["Sun", "Mercury", "Venus", "Jupiter"],
          "title": "4 Planets in Capricorn",
          "subtitle": "Tight Sign Stellium",
          "description": "You have a concentration of Sun, Mercury, Venus and Jupiter in Capricorn. This gives you ambition, discipline, and strong executive abilities. You approach goals methodically and can achieve significant long-term success. Having multiple planets in one sign creates an emphasis on these qualities in your personality and life experience."
        }
      ]
    }
  }
}
```

Note: The actual response will be dynamically generated based on the user's birth chart data. The above example is for illustrative purposes only. 