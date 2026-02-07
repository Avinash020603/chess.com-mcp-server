import requests

headers = {
    "User-Agent": "MCP-Chess-Stats-Bot/1.0 (your-email@example.com)"
}
CHESS_API_BASE="https://api.chess.com/pub"

def get_player_profile(username):
    url=f"{CHESS_API_BASE}/player/{username}"
    response=requests.get(url,headers=headers)
    response.raise_for_status()
    return response.json()

def get_player_stats(username):
    url=f"{CHESS_API_BASE}/player/{username}/stats"
    response=requests.get(url,headers=headers)
    response.raise_for_status()
    return response.json()

def get_player_current_games(username):
    url = f"{CHESS_API_BASE}/player/{username}/games"
    response = requests.get(url,headers=headers)
    response.raise_for_status()
    return response.json()


