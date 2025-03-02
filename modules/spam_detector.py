# modules/spam_detector.py
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Loading custom prebuilt model
def load_spam_model(model_dir="your_absolute_path\\pretrained\\v1"):
    """
    Loads the custom v1 spam detection model from the local directory.
    The directory should contain:
      - config.json
      - model.safetensors
      - special_tokens.map.json
      - tokenizer_config.json
      - vocab.txt
    """
    tokenizer = AutoTokenizer.from_pretrained(model_dir, local_files_only=True)
    model = AutoModelForSequenceClassification.from_pretrained(model_dir, local_files_only=True)
    return tokenizer, model


def predict_spam(email_text, tokenizer, model, threshold=0.5):
    inputs = tokenizer(email_text, return_tensors="pt", padding="max_length", truncation=True, max_length=128)
    outputs = model(**inputs)
    # Binary classification: output logits of shape [batch_size, 2]
    probs = outputs.logits.softmax(dim=-1)
    spam_score = probs[0][1].item()  # index 1 for spam class
    is_spam = spam_score >= threshold
    return is_spam, spam_score


if __name__ == "__main__":
    tokenizer, model = load_spam_model()
    sample_email = "Congratulations! You've won a free cruise. Click here to claim."
    is_spam, score = predict_spam(sample_email, tokenizer, model)
    print(f"Spam: {is_spam} (Score: {score:.2f})")
