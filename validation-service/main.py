from fastapi import FastAPI
from pydantic import BaseModel
from mlb_db import player_exists, team_correct

# Create instance of FastAPI app
app = FastAPI()

# Define Pydantic model for incoming request body
# Validates structure of data sent to API endpoint
class PlayerRequest(BaseModel):
    
    # Expecting a list of dictionaries, each representing a player with 'name' and 'team'
    players: list[dict]
    
# Define the POST endpoint '/validate' that will be used to validate player information
@app.post("/validate")
def validate_players(request: PlayerRequest):
    # Initialize an empty list to store results for each player
    results = []
    
    # Loop through each player in the incoming request's 'players' list
    for p in request.players:
        # Extract player's name and team from the dictionary
        name = p["name"]
        team = p["team"]
        
        # Check if the player exists
        exists = player_exists(name)
        
        # If the player exists, check if the player's team is correct
        if exists:
            correct_team = team_correct(name, team)
        else:
            correct_team = False
        
        # Append the results for this player to the results list
        results.append({
            "name": name,
            "team": team,
            "player_exists": exists,
            "team_correct": correct_team
        })
        
    # Return the reuslts as a JSON response
    return {"results": results}