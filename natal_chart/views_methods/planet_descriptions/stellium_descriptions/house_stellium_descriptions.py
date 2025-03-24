"""
House Stellium Descriptions

This module provides descriptions for stelliums (3 or more planets) in each house of the natal chart.
"""

def get_house_stellium_description(house):
    """
    Get the description for a stellium in a specific house.
    
    Args:
        house: The house number (1-12)
        
    Returns:
        Dictionary with title and description for the stellium
    """
    descriptions = {
        "1": {
            "title": "First House Stellium",
            "description": "With a stellium in the First House, your personality and physical presence are extraordinarily powerful. You make strong first impressions and possess a remarkable ability to project your identity into the world. This concentration of energy makes you self-reliant, assertive, and naturally inclined to take initiative in life. You may sometimes appear overwhelming to others or overly focused on personal concerns, but your vitality and authentic self-expression are invaluable gifts. You thrive when you can channel this powerful energy into pursuits that allow you to express your unique identity and pioneer new paths."
        },
        "2": {
            "title": "Second House Stellium",
            "description": "A stellium in the Second House gives you an exceptional relationship with material resources, personal values, and self-worth. You likely have pronounced talents for building security, managing resources, and creating comfort in your life and the lives of others. This concentration of energy makes you remarkably grounded, practical, and skilled at manifesting tangible results. You may sometimes appear possessive or overly concerned with material security, but your stability and ability to create value are profound strengths. You excel in situations that allow you to build something of lasting worth and establish secure foundations."
        },
        "3": {
            "title": "Third House Stellium",
            "description": "With a stellium in the Third House, you possess extraordinary communication abilities, intellectual curiosity, and adaptability. You're likely to be exceptionally articulate, mentally agile, and connected to your immediate environment and community. This concentration of energy makes you a natural learner, communicator, and networker who thrives on gathering and sharing information. You may sometimes appear scattered or overly talkative, but your mental flexibility and verbal dexterity are remarkable strengths. You excel in environments that offer variety, intellectual stimulation, and opportunities to connect with diverse people and ideas in your local sphere."
        },
        "4": {
            "title": "Fourth House Stellium",
            "description": "A stellium in the Fourth House gives you profound emotional depth, a strong connection to your roots, and exceptional nurturing abilities. You likely have a pronounced relationship with your home, family, and inner emotional life. This concentration of energy makes you incredibly intuitive, protective, and attuned to creating emotional security. You may sometimes appear overly private or emotionally guarded, but your depth of feeling and ability to create sanctuary are invaluable gifts. You thrive in situations where you can establish deep emotional foundations and create spaces of belonging for yourself and others."
        },
        "5": {
            "title": "Fifth House Stellium",
            "description": "With a stellium in the Fifth House, you possess extraordinary creative power, self-expression, and capacity for joy. You're likely to have exceptional talents in areas related to performance, artistry, romance, or working with children. This concentration of energy makes you remarkably playful, passionate, and dramatic in your approach to life. You may sometimes appear attention-seeking or self-centered, but your warmth and creative vitality are remarkable strengths. You excel when you can showcase your talents, engage in pleasurable pursuits, and receive recognition for your authentic self-expression."
        },
        "6": {
            "title": "Sixth House Stellium",
            "description": "A stellium in the Sixth House gives you exceptional analytical abilities, attention to detail, and a profound capacity for service and self-improvement. You likely have a pronounced desire for efficiency, order, and practical problem-solving in daily life. This concentration of energy makes you incredibly methodical, helpful, and skilled at refining systems and processes. You may sometimes appear critical or perfectionistic, but your precision and dedication to improvement are invaluable gifts. You thrive in situations that allow you to analyze, organize, and perfect the practical aspects of life and work."
        },
        "7": {
            "title": "Seventh House Stellium",
            "description": "With a stellium in the Seventh House, you possess extraordinary relationship skills, diplomatic abilities, and a profound orientation toward partnership. You're likely to be exceptionally attuned to others' needs and naturally inclined toward collaboration and cooperation. This concentration of energy makes you remarkably fair-minded, socially graceful, and skilled at creating harmony. You may sometimes appear overly accommodating or dependent on others' approval, but your interpersonal intelligence and sense of justice are remarkable strengths. You excel in partnerships and environments that value cooperation, balance, and mutual consideration."
        },
        "8": {
            "title": "Eighth House Stellium",
            "description": "A stellium in the Eighth House gives you profound emotional intensity, psychological insight, and transformative power. You likely have an exceptional ability to perceive hidden truths, navigate complex emotional terrain, and facilitate profound change. This concentration of energy makes you incredibly passionate, resourceful, and resilient in the face of crisis or challenge. You may sometimes appear secretive or controlling, but your depth and regenerative capacity are invaluable gifts. You thrive in situations that allow you to investigate mysteries, experience emotional intimacy, and facilitate profound transformation for yourself and others."
        },
        "9": {
            "title": "Ninth House Stellium",
            "description": "With a stellium in the Ninth House, you possess extraordinary vision, philosophical depth, and a natural orientation toward expansion and meaning. You're likely to be exceptionally truth-seeking, adventurous, and interested in broader cultural, educational, or spiritual horizons. This concentration of energy makes you a natural explorer who thrives on discovering new perspectives and meanings. You may sometimes appear dogmatic or restless, but your enthusiasm and wisdom are remarkable strengths. You excel when you can expand your horizons through travel, education, or spiritual pursuits, and when you can inspire others with your broad perspective."
        },
        "10": {
            "title": "Tenth House Stellium",
            "description": "A stellium in the Tenth House gives you exceptional ambition, discipline, and organizational ability in the public sphere. You likely have a pronounced sense of responsibility, authority, and drive toward achievement and recognition. This concentration of energy makes you incredibly determined, strategic, and oriented toward long-term goals and public contribution. You may sometimes appear status-conscious or overly focused on external success, but your leadership capacity and ability to create lasting structures are invaluable gifts. You thrive in situations that allow you to build a meaningful legacy and receive recognition for your contributions to society."
        },
        "11": {
            "title": "Eleventh House Stellium",
            "description": "With a stellium in the Eleventh House, you possess extraordinary social vision, humanitarian ideals, and community orientation. You're likely to be exceptionally group-minded, progressive, and concerned with collective welfare and future possibilities. This concentration of energy makes you a natural networker, innovator, and collaborator who values freedom and equality. You may sometimes appear detached or idealistic, but your inventiveness and social consciousness are remarkable strengths. You excel when you can collaborate with like-minded individuals on forward-thinking projects that benefit humanity and challenge outdated systems."
        },
        "12": {
            "title": "Twelfth House Stellium",
            "description": "A stellium in the Twelfth House gives you profound imagination, spiritual sensitivity, and access to collective unconscious realms. You likely have an exceptional ability to transcend boundaries, connect with universal energies, and perceive subtle dimensions of reality. This concentration of energy makes you incredibly empathetic, intuitive, and artistically or spiritually gifted. You may sometimes appear escapist or overly sensitive, but your mystical awareness and healing capacity are invaluable gifts. You thrive in environments that honor your sensitivity, allow for creative or spiritual expression, and provide opportunities to serve others through your unique gifts of compassion and vision."
        }
    }
    
    # Convert house to string if it's a number
    house_key = str(house)
    
    return descriptions.get(house_key, None) 