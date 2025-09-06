# Utility functions to support ai_engine.py
import re
from typing import List, Dict

def extract_keywords(text: str) -> List[str]:
    """Extracts keywords from a given text using simple regex."""
    # Remove punctuation and split by spaces
    words = re.findall(r'\b\w+\b', text.lower())
    # Filter out common stopwords (simple example)
    stopwords = {'the', 'is', 'at', 'which', 'on', 'and', 'a', 'an', 'of', 'for', 'to', 'in', 'with', 'by', 'this', 'that', 'it', 'as', 'but', 'or', 'be', 'are', 'was', 'were', 'has', 'have', 'had'}
    keywords = [word for word in words if word not in stopwords]
    return keywords

def summarize_email(email: Dict[str, str]) -> str:
    """Creates a simple summary from an email dict."""
    subject = email.get('subject', '')
    body = email.get('body', '')
    summary = f"Subject: {subject}\nSummary: {body[:100]}..."
    return summary
