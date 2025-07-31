def detect_fallacies(text: str):
    # Placeholder logic for demo/test purposes
    fallacies = []

    if "you" in text.lower() and "stupid" in text.lower():
        fallacies.append("ad_hominem")
    if "obviously" in text.lower():
        fallacies.append("begging_the_question")

    return fallacies
