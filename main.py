from fastapi import FastAPI
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key
API_KEY = os.getenv("FOOTBALL_API_KEY")
BASE_URL = "https://v3.football.api-sports.io"

# Initialize FastAPI app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Live Soccer Score Chatbot is running!"}

@app.get("/live_scores")
def get_live_scores():
    # Debug: Check if API_KEY is loaded
    print(f"[DEBUG] API Key: {API_KEY}")  # Should show your key, not None
    
    headers = {"x-apisports-key": API_KEY}
    response = requests.get(f"{BASE_URL}/fixtures?live=all", headers=headers)
    
    # Debug: Check API response
    print(f"[DEBUG] API Response: {response.status_code} - {response.text}")
    
    return response.json()

from dotenv import load_dotenv
load_dotenv()  # Loads variables from .env
API_KEY = os.getenv("FOOTBALL_API_KEY")
