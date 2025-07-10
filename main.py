from fastapi import FastAPI
import json
import os

app = FastAPI()

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

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
