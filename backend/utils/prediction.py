import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import pickle
import os

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "model"))

# 🔥 Load tokenizer directly from HuggingFace (no vocab.txt needed manually)
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

# Load your trained models
category_model = AutoModelForSequenceClassification.from_pretrained(
    os.path.join(BASE_PATH, "bert_ticket_model")
)

priority_model = AutoModelForSequenceClassification.from_pretrained(
    os.path.join(BASE_PATH, "bert_priority_model")
)

# Load encoders
with open(os.path.join(BASE_PATH, "category_encoder.pkl"), "rb") as f:
    category_encoder = pickle.load(f)

with open(os.path.join(BASE_PATH, "priority_encoder.pkl"), "rb") as f:
    priority_encoder = pickle.load(f)


def predict_ticket(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)

    with torch.no_grad():
        category_outputs = category_model(**inputs)
        priority_outputs = priority_model(**inputs)

    category_pred = torch.argmax(category_outputs.logits, dim=1).item()
    priority_pred = torch.argmax(priority_outputs.logits, dim=1).item()

    category = category_encoder.inverse_transform([category_pred])[0]
    priority = priority_encoder.inverse_transform([priority_pred])[0]

    return category, priority
