# MailSift AI

**MailSift AI** is an open-source, dual-function email processing model designed to both detect **spam and filter incoming emails** based on each user's unique preferences. It leverages state-of-the-art transformer architectures (e.g., fine-tuned BERT) for spam detection while incorporating explicit user feedback to prioritize emails that matter most.

The goal is to create a robust AI model capable of filtering out spam and unwanted emails for all citizens. As mentioned by Emailtooltester.com in their "Spam Statistics 2025" article: _"160 billion spam emails are sent every day, with 46% of the 347 billion daily emails sent, considered spam (numbers recorded for 2023). The majority of people (96.8%) have received spam messages in some form."_

Ideally, MailSift AI model working with Gmail, Outlook and other email platforms could enhance general security significantly (addressing money scams, phishing, malware, botnets, refund scams, fake dating, call spams and many more) and enhancing filtering for emails by user-preferrence.

Successive models will be created, improving on each version, trained on more data and finetuned in certain parameters.

The project is more than open to be expanded, improved, communicated and be considered by the tech community. However, author of this project is Krish Sadhwani, with MIT license clarifying original ownership and attribution requirements, contribution guidelines can be found in `CONTRIBUTING.md`.

## Features

- **Spam Detection:** Uses a fine-tuned BERT-based model to classify emails as spam or not spam.
- **User Preference Filtering:** Filters and prioritizes emails based on explicit feedback (likes/dislikes) provided by the user.
- **Modular Design:** Easily extendable architecture with separate modules for spam detection and user preference scoring.
- **Open-Source & Community-Driven:** Contributions are welcome. All contributions will retain original attribution to the project owner.

## Mail Spam Detection Model

v1 model can be found: https://huggingface.co/KrishT97/spam-mail-detection/tree/main

## Dataset and Model Training

### For v1: 

The training data was created by merging two Kaggle email spam detection datasets—each containing text and label (binary values indicating "Spam" or "Not Spam") fields—to form a comprehensive CSV file with approximately 10,000 entries. The resulting dataset provided a balanced mix of spam and non-spam examples that were used to fine-tune the `bert-base-uncased` model for our binary classification task.

Emails typically beginning with "Subject: " and all types of body responses consisting of replies, promotion, urgent messages, meetings, events, bookings..etc

More information on the technical details on the model approach can be found: https://huggingface.co/KrishT97/spam-mail-detection/blob/main/pretrained/README.md

## Project Structure
```bash
MailSift-AI/ 
├── README.md 
├── LICENSE 
├── CONTRIBUTING.md  
├── main.py 
├── pretrained # Pretrained folder can be found within HuggingFace link in "Mail Spam Detection Model" section
├── modules/ │ 
             ├── init.py 
             ├── spam_detector.py # Loads the custom v1 model and predicts spam probability. 
             ├── user_preference.py # Scores emails based on explicit user feedback. 
             ├── mail_sorter.py # Combines spam detection and preference scoring. 
├── data/ │ 
          ├── emails_sample.json # Sample emails organized by persona. 
          ├── user_feedback.json # User preferences (likes/dislikes) per persona. 
├── requirements.txt
```

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/MailSift-AI.git
   cd MailSift-AI
   ```

2. **Create a virtual environment and install dependencies:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Place the custom model files:**

   Ensure that the custom model (v1) files – `config.json, model.safetensors, special_tokens.map.json, tokenizer_config.json, and vocab.txt` – are placed in the _pretrained/v1/_ directory. Place the pretrained directory from the HuggingFace model repository: https://huggingface.co/KrishT97/spam-mail-detection/tree/main,
into the project directory:
   
## Usage

To run a prototype test that sorts sample emails for different people:
  ```bash
   python main.py
   ```
You will see output indicating the classification (spam/high priority/low priority) for each email based on the user's explicit preferences.

## Example Use Case

### v1

- Person 1 is an **office worker** and has received  2 emails.
- Person 2 is a **university student** and has received 3 emails.
- Person 3 is a **businessman** and has received 3 emails.
- Person 4 is a **housewife** and has received 2 emails.

Clearly the model does not know the people personally, but it can be fed certain interests (likes and dislikes) to know users preference.

Upon using MailSift-AI, the input data as follows:

_user_feedback.json_:
```bash
{
  "Person1": {
    "likes": ["meeting", "agenda", "report", "review"],
    "dislikes": ["free", "prize", "discount"]
  },
  "Person2": {
    "likes": ["assignment", "deadline", "campus", "tech talk"],
    "dislikes": ["offer", "free", "prize"]
  },
  "Person3": {
    "likes": ["investment", "market", "networking", "business"],
    "dislikes": ["free", "prize", "discount"]
  },
  "Person4": {
    "likes": ["grocery", "recipe", "dinner", "discount"],
    "dislikes": ["spam", "offer", "free"]
  }
}
```  
_email_samples.json_:

```bash
{
  "Person1": [
    {
      "id": "email001",
      "content": "Meeting agenda for tomorrow is attached. Please review the report and prepare your feedback."
    },
    {
      "id": "email002",
      "content": "Reminder: Quarterly performance review meeting is scheduled at 3 PM today in Conference Room B."
    }
  ],
  "Person2": [
    {
      "id": "email001",
      "content": "Your assignment deadline is approaching. Don't forget to submit your work by Friday evening."
    },
    {
      "id": "email002",
      "content": "Campus event: Join us for a tech talk on innovation in education and win exciting prizes."
    },
    {
      "id": "email003",
      "content": "Exclusive offer: Get 50% off on gaming accessories this weekend only. Level up your gaming experience!"
    }
  ],
  "Person3": [
    {
      "id": "email001",
      "content": "Exclusive investment opportunity: Our latest market analysis indicates significant growth in the tech sector."
    },
    {
      "id": "email002",
      "content": "Invitation: Attend a high-level business networking event at the downtown conference center this Thursday."
    },
    {
      "id": "email003",
      "content": "Hackathon announcement: Join us this weekend to innovate, compete, and win exciting prizes."
    }
  ],
  "Person4": [
    {
      "id": "email001",
      "content": "This week's grocery deals are here! Save on your favorite brands and enjoy special discounts."
    },
    {
      "id": "email002",
      "content": "New recipe alert: Delicious and healthy dinner ideas for your family are waiting for you."
    }
  ]
}
```

Upon processing, the AI model delivers the following results in a few seconds (running main.py).
The custom detection model processes the email content if it is Spam or Not Spam, if the email is Spam, it will print 'Spam' and its spam score. If the email is Not Spam, it will be further analyzed by the user preference sorting algorithm, which will identify if the email is of High Priority or Low Priority.
:

```bash
Results for Person1:
Email ID: email001 -> {'status': 'High Priority', 'relevance_score': 4, 'status_spam': 'Not Spam', 'spam_score': 2.6603707738104276e-05}
Email ID: email002 -> {'status': 'High Priority', 'relevance_score': 2, 'status_spam': 'Not Spam', 'spam_score': 1.7127618775703013e-05}

Results for Person2:
Email ID: email001 -> {'status': 'High Priority', 'relevance_score': 2, 'status_spam': 'Not Spam', 'spam_score': 5.382084418670274e-05}
Email ID: email002 -> {'status': 'Spam', 'spam_score': 0.9979434609413147}
Email ID: email003 -> {'status': 'Spam', 'spam_score': 0.9998857975006104}

Results for Person3:
Email ID: email001 -> {'status': 'Spam', 'spam_score': 0.9982413053512573}
Email ID: email002 -> {'status': 'High Priority', 'relevance_score': 2, 'status_spam': 'Not Spam', 'spam_score': 6.038564242771827e-05}
Email ID: email003 -> {'status': 'Spam', 'spam_score': 0.9855524897575378}

Results for Person4:
Email ID: email001 -> {'status': 'High Priority', 'relevance_score': 2, 'status_spam': 'Not Spam', 'spam_score': 0.0026375730521976948}
Email ID: email002 -> {'status': 'Spam', 'spam_score': 0.999722421169281}
```

The following content of emails were detected as spam through the custom model:

For Student (Person 2):
- "Campus event: Join us for a tech talk on innovation in education and win exciting prizes."
- "Exclusive offer: Get 50% off on gaming accessories this weekend only. Level up your gaming experience!"

For Businessman (Person 3):
- "Exclusive investment opportunity: Our latest market analysis indicates significant growth in the tech sector."
- "Hackathon announcement: Join us this weekend to innovate, compete, and win exciting prizes."

For Housewife (Person 4):
- "New recipe alert: Delicious and healthy dinner ideas for your family are waiting for you."

## License and Attribution

This project is licensed under the terms defined in the LICENSE file. All contributions must maintain proper attribution to the original project owner.

## Contributing

We welcome contributions! Please see CONTRIBUTING.md for details on our code of conduct, contribution guidelines, and how to submit pull requests.

## Contact
For any questions or suggestions, please open an issue or contact the project owner Krish Sadhwani at techination.official@gmail.com

