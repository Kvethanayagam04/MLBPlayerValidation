# MLB Player Validation Service

## Overview

This project is a simple application that validates whether a listed baseball player is in Major League Baseball and whether the team associated with that player is correct.

Users provide a list of players and teams, and the system returns validation results indicating whether the player exists and whether the team listed matches the known team for that player.

Example input:

Shohei Ohtani, Dodgers  
Mike Trout, Yankees  
Fake Player, Blue Jays  

Example output:

Shohei Ohtani — Player Exists: True, Team Correct: True  
Mike Trout — Player Exists: True, Team Correct: False  
Fake Player — Player Exists: False, Team Correct: False  

## Technologies Used

Python  
FastAPI  
Uvicorn  
JavaScriptz
HTML  

## Running the Project

Start the validation service:

cd validation-service
uvicorn main:app --reload

Start the client backend:

cd client-backend
uvicorn main:app --port 5000 --reload

Open the frontend:

Open `client-frontend/index.html` in a browser.