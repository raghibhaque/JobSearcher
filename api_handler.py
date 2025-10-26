import requests
import os
from dotenv import load_dotenv

load_dotenv()

def summarize_text(text):
    """Summarizes text using Hugging Face API."""
    api_key = os.getenv("HUGGINGFACE_API_KEY")
    headers = {"Authorization": f"Bearer {api_key}"}
    data = {"inputs": text[:1000]}  # limit text length for free API

    response = requests.post(
        "https://api-inference.huggingface.co/models/facebook/bart-large-cnn",
        headers=headers, json=data
    )

    if response.status_code == 200:
        summary = response.json()[0]["summary_text"]
        return summary
    else:
        return "Summary unavailable (API limit or error)"
