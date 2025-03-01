# modules/user_preference.py
import json


def load_user_profile(user_id, feedback_file="data/user_feedback.json"):
    # For simplicity, loading a JSON file where each user has a profile of liked/disliked keywords
    with open(feedback_file, "r") as f:
        profiles = json.load(f)
    return profiles.get(user_id, {"likes": [], "dislikes": []})


def score_email(email_text, user_profile):
    # Simple keyword matching approach for v1
    score = 0
    for keyword in user_profile.get("likes", []):
        if keyword.lower() in email_text.lower():
            score += 1
    for keyword in user_profile.get("dislikes", []):
        if keyword.lower() in email_text.lower():
            score -= 1
    return score

