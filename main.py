# main.py
import json
from modules import spam_detector, mail_sorter


def load_emails(email_file="data/emails_sample.json"):
    with open(email_file, "r") as f:
        return json.load(f)


def load_user_feedback(feedback_file="data/user_feedback.json"):
    with open(feedback_file, "r") as f:
        return json.load(f)


def main():
    # Loading custom spam detection model
    tokenizer, spam_model = spam_detector.load_spam_model()

    # Loading emails and user feedback JSON files
    emails_by_person = load_emails()
    user_feedback = load_user_feedback()

    # Iterating through each person in the feedback file
    for person, profile in user_feedback.items():
        print(f"\nResults for {person}:")
        # Getting the sample emails for this person
        sample_emails = emails_by_person.get(person, [])
        if not sample_emails:
            print(f"No emails found for {person}.")
            continue

        # Processing each email for the person
        for email in sample_emails:
            result = mail_sorter.sort_email(email, tokenizer, spam_model, profile)
            print(f"Email ID: {email['id']} -> {result}")


if __name__ == "__main__":
    main()

