PLAYERS = {
    "shohei ohtani" : "dodgers",
    "aaron judge" : "yankees",
    "mike trout" : "angels",
    "mookie betts" : "dodgers",
    "vladimir guerrero jr": "blue jays"
}

def player_exists(name):
    """
    Check if the given name is in the players database
    """
    
    return name.lower() in PLAYERS

def team_correct(name, team):
    """
    Check if the provided team for the given player is correct
    """
    
    # Check if the player exists first
    if not player_exists(name):
        return False
    
    correct_team = PLAYERS[name.lower()]
    
    return correct_team == team.lower()