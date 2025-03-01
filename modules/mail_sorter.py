# modules/mail_sorter.py
from modules import spam_detector, user_preference


def sort_email(email, tokenizer, spam_model, user_profile, spam_threshold=0.5, relevance_threshold=1):
    # Spam detection
    is_spam, spam_score = spam_detector.predict_spam(email["content"], tokenizer, spam_model, threshold=spam_threshold)
    if is_spam:
        return {"status": "Spam", "spam_score": spam_score}

    # User preference filtering
    relevance_score = user_preference.score_email(email["content"], user_profile)
    if relevance_score >= relevance_threshold:
        return {"status": "High Priority", "relevance_score": relevance_score, "status_spam": "Not Spam",
                "spam_score": spam_score}
    else:
        return {"status": "Low Priority", "relevance_score": relevance_score, "status_spam": "Not Spam",
                "spam_score": spam_score}
