from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# A place to store the current game state
current_card = []
called_numbers = set()

# Functions for the core bingo logic
def generate_bingo_card():
    card = {}
    
    # Generate numbers for each column (B, I, N, G, O)
    card['B'] = random.sample(range(1, 16), 5)
    card['I'] = random.sample(range(16, 31), 5)
    card['N'] = random.sample(range(31, 46), 5)
    card['G'] = random.sample(range(46, 61), 5)
    card['O'] = random.sample(range(61, 76), 5)

    # The center square is "free"
    card['N'][2] = 'FREE'
    
    return card

def check_for_bingo(card, numbers_called):
    # Flatten the card for easy access
    flat_card = []
    for col in ['B', 'I', 'N', 'G', 'O']:
        flat_card.extend(card[col])

    # Winning combinations (rows, columns, diagonals)
    winning_combinations = [
        # Rows
        (0, 1, 2, 3, 4), (5, 6, 7, 8, 9), (10, 11, 12, 13, 14), (15, 16, 17, 18, 19), (20, 21, 22, 23, 24),
        # Columns
        (0, 5, 10, 15, 20), (1, 6, 11, 16, 21), (2, 7, 12, 17, 22), (3, 8, 13, 18, 23), (4, 9, 14, 19, 24),
        # Diagonals
        (0, 6, 12, 18, 24), (4, 8, 12, 16, 20)
    ]

    # Check each combination for a winner
    for combo in winning_combinations:
        is_bingo = True
        for index in combo:
            number = flat_card[index]
            if number != 'FREE' and number not in numbers_called:
                is_bingo = False
                break
        if is_bingo:
            return True
    
    return False

# ----- API Endpoints -----
@app.route("/api/new_card", methods=['GET'])
def get_new_card():
    """Generates and returns a new bingo card."""
    global current_card
    current_card = generate_bingo_card()
    return jsonify(current_card)

@app.route("/")
def home():
    return "Welcome to the Bingo App Backend!"

@app.route("/api/status")
def status():
    return jsonify({"status": "Backend is running!"})

# To run the server, we'll use this block of code.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
