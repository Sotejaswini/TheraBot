CRISIS_KEYWORDS = ["suicide", "kill myself", "end my life", "depressed", "hopeless"]

def check_crisis_keywords(user_input: str):
    text = user_input.lower()
    for word in CRISIS_KEYWORDS:
        if word in text:
            return True, "If you are in crisis, please call your regional helpline (e.g., 988 in the US)."
    return False, None
