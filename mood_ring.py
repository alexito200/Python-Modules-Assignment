def mood_response(mood):
    mood = mood.lower()
    if mood in ["happy", "excited", "joyful"]:
        return "That's great to hear! Keep smiling!"
    elif mood in ["sad", "down", "unhappy"]:
        return "I'm sorry you're feeling that way. I'm here for you!"
    elif mood in ["angry", "frustrated"]:
        return "Take a deep breath, it'll be okay!"
    elif mood in ["tired", "exhausted"]:
        return "You should take some rest and recharge!"
    else:
        return "Thank you for sharing! I hope you have a wonderful day!"