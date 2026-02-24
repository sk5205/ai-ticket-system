import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load model directly from HuggingFace
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

category_model = AutoModelForSequenceClassification.from_pretrained(
    "distilbert-base-uncased"
)

priority_model = AutoModelForSequenceClassification.from_pretrained(
    "distilbert-base-uncased"
)

# Dummy labels (adjust if needed)
categories = ["Hardware", "Software", "Network", "Access", "Storage"]
priorities = ["Low", "Medium", "High"]


def predict_ticket(text):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    with torch.no_grad():
        category_outputs = category_model(**inputs)
        priority_outputs = priority_model(**inputs)

    category_pred = torch.argmax(category_outputs.logits, dim=1).item()
    priority_pred = torch.argmax(priority_outputs.logits, dim=1).item()

    category = categories[category_pred % len(categories)]
    priority = priorities[priority_pred % len(priorities)]

    return category, priority