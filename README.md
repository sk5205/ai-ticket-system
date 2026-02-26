🚀 AI-Powered Ticket Classification System

An intelligent support ticket system built using FastAPI and BERT (Transformers) that automatically predicts ticket Category and Priority using Natural Language Processing (NLP).

This project demonstrates end-to-end integration of a machine learning model with a web-based ticketing application.

🎯 Project Overview

Traditional ticket systems require manual categorization and priority assignment.
This system automates that process using a fine-tuned BERT model.

Workflow:

User Input → AI Prediction (Category & Priority) → Database Storage → Dashboard Display

🚀 Key Features


1️⃣ Ticket Submission

User-friendly HTML form

Ticket description input

Backend validation using Pydantic

2️⃣ AI-Based Classification

BERT-based text classification

Automatic category prediction

Automatic priority prediction

Separate LabelEncoders for category and priority

3️⃣ Backend (FastAPI)

REST API endpoints

Model loaded at startup

Prediction endpoint

Error handling using try-except

4️⃣ Database Integration

MySQL database

Ticket table schema

Stores:

Description

Predicted Category

Predicted Priority

Timestamp

5️⃣ Dashboard

Displays submitted tickets

Shows predicted results

Simple and responsive UI

🛠️ Technology Stack
Backend

Python 3.9+

FastAPI

Uvicorn

SQLAlchemy / MySQL Connector

AI Model

BERT (HuggingFace Transformers)

PyTorch

Scikit-learn (LabelEncoder)

Database

MySQL

Frontend

HTML

CSS

Basic JavaScript (if used)

🤖 AI Model Details

Pretrained BERT base model

Fine-tuned on ticket dataset

Separate training for:

Category classification

Priority classification

Model saved using:

torch.save()

Encoders saved as:

category_encoder.pkl

priority_encoder.pkl

📊 Performance

FastAPI inference time: ~400–800ms (CPU)

Optimized by loading model once at startup

Separate encoder mapping ensures correct label decoding

🔒 Security & Validation

Input validation using Pydantic

No hardcoded credentials

Environment-based configuration

Basic error handling implemented
