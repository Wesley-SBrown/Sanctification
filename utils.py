# utils.py
import prayers

def pray(emotion):
    prayers_dict = {
        "joy": prayers.joy_prayer,
        "anxiety": prayers.anxiety_prayer,
        "loneliness": prayers.loneliness_prayer,
        "anger": prayers.anger_prayer,
        "gratitude": prayers.gratitude_prayer,
        "confusion": prayers.confusion_prayer,
        "despair": prayers.despair_prayer,
        "love": prayers.love_prayer,
        "self_doubt": prayers.self_doubt_prayer,
        "awe": prayers.awe_prayer,
        "dryness": prayers.dryness_prayer,  # when you feel nothing
        "fear": prayers.fear_prayer
    }
    emojis = {
        "joy": "😄",
        "anxiety": "😰",
        "loneliness": "🥺",
        "anger": "😡",
        "gratitude": "🙏",
        "confusion": "🤯",
        "despair": "💔",
        "love": "❤️",
        "self_doubt": "😔",
        "awe": "🌌",
        "dryness": "😶",
        "fear": "😨"
    }
    print(f"Running prayer for: {emotion.upper()} {emojis.get(emotion)}")


    return prayers_dict.get(emotion.lower(), prayers.default_prayer())
