from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

# Create instance of FastAPI app
app = FastAPI()

# Allow frontend requests
# Needed because index file opened as "file:///index.html" while backend is "http://localhost:5000" so they are different origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all origins for now
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# URL of validation service that the app will communicate with
VALIDATION_URL = "http://localhost:8000/validate"

# Define the POST endpoint '/check' that will be used to check player information
@app.post("/check_players")
def check_player(data: dict):
    """
    Endpoint that receives player data and sends it to the validation service.
    The validation service is expected to validate the player info and return the result.
    """
    
    # Make a POST request to the validation service with the given data
    response = requests.post(
        VALIDATION_URL,
        json=data
    )
    
    # Return the JSON response from the validation service
    return response.json()