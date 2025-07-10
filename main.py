from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import json
import os

app = FastAPI()

# Load data
with open("data.json", "r") as f:
    data = json.load(f)

@app.get("/")
def root():
    return {"message": "Welcome to the Video Game Stats API!"}

@app.get("/games")
def get_all_games():
    return data

@app.get("/games/{rank}")
def get_game_by_rank(rank: int):
    for game in data:
        if game["game_rank"] == rank:
            return game
    return {"error": "Game not found"}

@app.get("/search", response_class=HTMLResponse)
async def search_form(request: Request, rank: int = None):
    if rank is None:
        return """
        <h2>Enter Game Rank to see Stats</h2>
        <form method="get">
            <input type="number" name="rank" placeholder="Enter rank (1-20)">
            <button type="submit">Get Stats</button>
        </form>
        """

    # find game
    game = next((g for g in data if g["game_rank"] == rank), None)
    if game:
        return f"""
        <h2>Stats for Game Rank {rank}</h2>
        <ul>
            <li><b>Game Name:</b> {game['game_name']}</li>
            <li><b>Total Players:</b> {game['total_players']}</li>
            <li><b>Top Player:</b> {game['top_player']}</li>
            <li><b>Difficulty:</b> {game['difficulty']}</li>
            <li><b>Top 5 Players:</b> {', '.join(game['top_5_players'])}</li>
            <li><b>Average Game Length:</b> {game['average_game_length']} min</li>
        </ul>
        <a href="/search">Search Again</a>
        """
    else:
        return f"""
        <h2>No game found with rank {rank}</h2>
        <a href="/search">Try again</a>
        """
