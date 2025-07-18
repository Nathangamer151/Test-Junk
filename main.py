from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import json

app = FastAPI()

# Load data
with open("data.json", "r") as f:
    data = json.load(f)

@app.get("/", response_class=HTMLResponse)
async def root(request: Request, rank: int = None):
    style = """
    <style>
    body {
        font-family: Arial, sans-serif;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        flex-direction: column;
        background: #f9f9f9;
    }
    form, ul, h2, a {
        text-align: center;
    }
    input, button {
        padding: 8px;
        margin: 5px;
        font-size: 16px;
    }
    </style>
    """

    if rank is None:
        return style + """
        <h2>Enter Game Rank to see Stats</h2>
        <form method="get">
            <input type="number" name="rank" placeholder="Enter rank (1-20)">
            <button type="submit">Get Stats</button>
        </form>
        """

    game = next((g for g in data if g["game_rank"] == rank), None)
    if game:
        return style + f"""
        <h2>Stats for Game Rank {rank}</h2>
        <ul>
            <li><b>Game Name:</b> {game['game_name']}</li>
            <li><b>Total Players:</b> {game['total_players']}</li>
            <li><b>Top Player:</b> {game['top_player']}</li>
            <li><b>Difficulty:</b> {game['difficulty']}</li>
            <li><b>Top 5 Players:</b> {', '.join(game['top_5_players'])}</li>
            <li><b>Average Game Length:</b> {game['average_game_length']} min</li>
        </ul>
        <a href="/">Search Again</a>
        """
    else:
        return style + f"""
        <h2>No game found with rank {rank}</h2>
        <a href="/">Try again</a>
        """
