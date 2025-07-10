import json

# Load data
with open("data.json", "r") as f:
    data = json.load(f)

while True:
    user_input = input("\nEnter game rank (1-20) or 'exit' to quit: ").strip()
    if user_input.lower() == "exit":
        break

    if not user_input.isdigit():
        print("Please enter a valid number.")
        continue

    rank = int(user_input)
    game = next((g for g in data if g["game_rank"] == rank), None)

    if game:
        print(f"\n🎮 {game['game_name']}")
        print(f"Total Players: {game['total_players']}")
        print(f"Top Player: {game['top_player']}")
        print(f"Difficulty: {game['difficulty']}")
        print(f"Top 5 Players: {', '.join(game['top_5_players'])}")
        print(f"Average Game Length: {game['average_game_length']} min")
    else:
        print("No game found with that rank.")
