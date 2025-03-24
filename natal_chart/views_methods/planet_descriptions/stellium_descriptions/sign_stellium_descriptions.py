"""
Sign Stellium Descriptions

This module provides descriptions for stelliums (3 or more planets) in each zodiac sign.
"""

def get_sign_stellium_description(sign):
    """
    Get the description for a stellium in a specific zodiac sign.
    
    Args:
        sign: The zodiac sign name
        
    Returns:
        Dictionary with title and description for the stellium
    """
    descriptions = {
        "Aries": {
            "title": "Aries Stellium",
            "description": "With a stellium in Aries, you possess an extraordinary amount of initiative, courage, and pioneering spirit. You're likely to be extremely self-motivated, independent, and action-oriented. This concentration of energy makes you a natural leader who isn't afraid to forge new paths and take risks. You may sometimes come across as impulsive or overly competitive, but your enthusiasm and determination are unmatched. You thrive when you can channel this powerful energy into meaningful pursuits that allow you to express your individuality and make an impact."
        },
        "Taurus": {
            "title": "Taurus Stellium",
            "description": "A stellium in Taurus gives you exceptional determination, practicality, and a strong connection to the material world. You likely have a pronounced appreciation for beauty, comfort, and quality in all things. This concentration of energy makes you incredibly reliable, patient, and persistent in pursuing your goals. You may sometimes appear stubborn or resistant to change, but your stability and sensual awareness are profound gifts. You excel when you can build something of lasting value and enjoy the fruits of your labor in tangible ways."
        },
        "Gemini": {
            "title": "Gemini Stellium",
            "description": "With a stellium in Gemini, you possess extraordinary mental agility, curiosity, and communication skills. You're likely to be exceptionally versatile, quick-witted, and socially adaptable. This concentration of energy makes you a natural learner who thrives on gathering and sharing information. You may sometimes appear scattered or inconsistent, but your intellectual flexibility and verbal dexterity are remarkable strengths. You excel in environments that offer variety, intellectual stimulation, and opportunities to connect with diverse people and ideas."
        },
        "Cancer": {
            "title": "Cancer Stellium",
            "description": "A stellium in Cancer gives you profound emotional sensitivity, nurturing abilities, and intuitive understanding. You likely have a deep connection to your roots, family, and home life. This concentration of energy makes you exceptionally protective, empathetic, and attuned to the needs of others. You may sometimes appear moody or overly cautious, but your emotional intelligence and caring nature are invaluable gifts. You thrive in situations where you can create emotional security for yourself and others, and where your natural caretaking abilities are appreciated."
        },
        "Leo": {
            "title": "Leo Stellium",
            "description": "With a stellium in Leo, you possess extraordinary creative power, charisma, and self-expression. You're likely to have a strong sense of identity and natural leadership abilities. This concentration of energy makes you exceptionally confident, generous, and dramatic in your approach to life. You may sometimes appear domineering or attention-seeking, but your warmth and creative vitality are remarkable strengths. You excel when you can showcase your talents, inspire others, and receive recognition for your authentic self-expression."
        },
        "Virgo": {
            "title": "Virgo Stellium",
            "description": "A stellium in Virgo gives you exceptional analytical abilities, attention to detail, and practical problem-solving skills. You likely have a pronounced desire for improvement, efficiency, and order in all areas of life. This concentration of energy makes you incredibly methodical, service-oriented, and discriminating. You may sometimes appear critical or perfectionistic, but your precision and helpfulness are invaluable gifts. You thrive in situations that allow you to analyze, refine, and perfect systems and processes."
        },
        "Libra": {
            "title": "Libra Stellium",
            "description": "With a stellium in Libra, you possess extraordinary diplomatic skills, aesthetic sensitivity, and a profound sense of fairness. You're likely to be exceptionally relationship-oriented, harmonious, and socially graceful. This concentration of energy makes you a natural mediator who strives for balance and beauty in all things. You may sometimes appear indecisive or overly accommodating, but your tact and sense of justice are remarkable strengths. You excel in partnerships and environments that value cooperation, refinement, and mutual consideration."
        },
        "Scorpio": {
            "title": "Scorpio Stellium",
            "description": "A stellium in Scorpio gives you profound emotional intensity, psychological insight, and transformative power. You likely have an exceptional ability to perceive hidden truths and navigate complex emotional terrain. This concentration of energy makes you incredibly passionate, resourceful, and resilient. You may sometimes appear secretive or controlling, but your depth and regenerative capacity are invaluable gifts. You thrive in situations that allow you to investigate mysteries, experience emotional intimacy, and facilitate profound transformation."
        },
        "Sagittarius": {
            "title": "Sagittarius Stellium",
            "description": "With a stellium in Sagittarius, you possess extraordinary vision, optimism, and philosophical breadth. You're likely to be exceptionally freedom-loving, truth-seeking, and expansive in your worldview. This concentration of energy makes you a natural explorer who thrives on adventure and meaning. You may sometimes appear blunt or restless, but your enthusiasm and wisdom are remarkable strengths. You excel when you can expand your horizons through travel, education, or spiritual pursuits, and when you can inspire others with your broad perspective."
        },
        "Capricorn": {
            "title": "Capricorn Stellium",
            "description": "A stellium in Capricorn gives you exceptional ambition, discipline, and organizational ability. You likely have a pronounced sense of responsibility, practicality, and respect for tradition. This concentration of energy makes you incredibly determined, patient, and strategic in pursuing long-term goals. You may sometimes appear stern or status-conscious, but your reliability and capacity for achievement are invaluable gifts. You thrive in structured environments that reward hard work, integrity, and the ability to build enduring legacies."
        },
        "Aquarius": {
            "title": "Aquarius Stellium",
            "description": "With a stellium in Aquarius, you possess extraordinary originality, humanitarian vision, and intellectual independence. You're likely to be exceptionally progressive, innovative, and community-minded. This concentration of energy makes you a natural visionary who values freedom and equality. You may sometimes appear detached or eccentric, but your inventiveness and social consciousness are remarkable strengths. You excel when you can collaborate with like-minded individuals on forward-thinking projects that benefit humanity and challenge outdated systems."
        },
        "Pisces": {
            "title": "Pisces Stellium",
            "description": "A stellium in Pisces gives you profound imagination, compassion, and spiritual sensitivity. You likely have an exceptional ability to transcend boundaries and connect with universal energies. This concentration of energy makes you incredibly empathetic, intuitive, and artistically gifted. You may sometimes appear escapist or impressionable, but your mystical awareness and healing capacity are invaluable gifts. You thrive in environments that honor your sensitivity, allow for creative expression, and provide opportunities to serve others through your unique spiritual gifts."
        }
    }
    
    return descriptions.get(sign, None) 