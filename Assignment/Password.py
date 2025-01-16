import requests
import random
import time
import os
import json

LEADERBOARD_FILE = "leaderboard.txt"
STATS_FILE = "player_stats.json"

def fetch_categories():
    """Fetch available categories from the API."""
    url = "https://opentdb.com/api_category.php"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("trivia_categories", [])
    else:
        print("Failed to fetch categories.")
        return []

def fetch_trivia_questions(amount=5, difficulty="medium", category=None):
    """Fetch trivia questions with specified difficulty and category."""
    url = f"https://opentdb.com/api.php?amount={amount}&difficulty={difficulty}&type=multiple"
    if category:
        url += f"&category={category}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        print("Failed to fetch trivia questions.")
        return []

def display_question(question_data, question_number):
    """Display a single question with answer choices."""
    print(f"\nQuestion {question_number}: {question_data['question']}")
    choices = question_data["incorrect_answers"] + [question_data["correct_answer"]]
    random.shuffle(choices)
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")
    return choices

def save_score(player_name, score):
    """Save the player's score to the leaderboard."""
    with open(LEADERBOARD_FILE, "a") as file:
        file.write(f"{player_name},{score}\n")

def display_leaderboard():
    """Display the leaderboard."""
    if not os.path.exists(LEADERBOARD_FILE):
        print("\nNo leaderboard data available.")
        return

    print("\n--- Leaderboard ---")
    with open(LEADERBOARD_FILE, "r") as file:
        scores = [line.strip().split(",") for line in file.readlines()]
        sorted_scores = sorted(scores, key=lambda x: int(x[1]), reverse=True)[:10]
        for i, (name, score) in enumerate(sorted_scores, 1):
            print(f"{i}. {name} - {score} points")

def load_player_stats():
    """Load player statistics from the file."""
    if not os.path.exists(STATS_FILE):
        return {}
    with open(STATS_FILE, "r") as file:
        return json.load(file)

def save_player_stats(stats):
    """Save player statistics to the file."""
    with open(STATS_FILE, "w") as file:
        json.dump(stats, file, indent=4)

def update_player_stats(player_name, questions_answered, score):
    """Update the player's statistics."""
    stats = load_player_stats()
    if player_name not in stats:
        stats[player_name] = {"games_played": 0, "total_questions": 0, "total_score": 0}

    stats[player_name]["games_played"] += 1
    stats[player_name]["total_questions"] += questions_answered
    stats[player_name]["total_score"] += score

    save_player_stats(stats)

def display_player_stats(player_name):
    """Display the player's statistics."""
    stats = load_player_stats()
    if player_name in stats:
        player_stats = stats[player_name]
        win_rate = (player_stats["total_score"] / player_stats["total_questions"] * 100) if player_stats["total_questions"] > 0 else 0
        print(f"\n--- Player Stats for {player_name} ---")
        print(f"Games Played: {player_stats['games_played']}")
        print(f"Total Questions Answered: {player_stats['total_questions']}")
        print(f"Total Score: {player_stats['total_score']}")
        print(f"Win Rate: {win_rate:.2f}%")
    else:
        print("\nNo statistics found for this player.")

def play_game():
    print("Welcome to the Enhanced Trivia Game!")

    # Get player's name
    player_name = input("Enter your name: ")

    # Display player stats
    display_player_stats(player_name)

    # Fetch categories and display them
    categories = fetch_categories()
    if categories:
        print("\nAvailable Categories:")
        for category in categories:
            print(f"{category['id']}: {category['name']}")
        try:
            selected_category = int(input("\nChoose a category by entering its ID (or press Enter for random): "))
        except ValueError:
            selected_category = None
    else:
        print("No categories available. Using random category.")
        selected_category = None

    # Ask for difficulty level
    difficulty = input("\nChoose a difficulty level (easy, medium, hard): ").lower()
    if difficulty not in ["easy", "medium", "hard"]:
        print("Invalid difficulty. Defaulting to medium.")
        difficulty = "medium"

    # Ask for the number of questions
    try:
        num_questions = int(input("\nEnter the number of questions (default is 5): "))
        if num_questions <= 0:
            raise ValueError
    except ValueError:
        print("Invalid number. Defaulting to 5.")
        num_questions = 5

    # Ask for a custom time limit
    try:
        time_limit = int(input("\nEnter the time limit per question in seconds (default is 15): "))
        if time_limit <= 0:
            raise ValueError
    except ValueError:
        print("Invalid time limit. Defaulting to 15 seconds.")
        time_limit = 15

    # Fetch questions
    questions = fetch_trivia_questions(amount=num_questions, difficulty=difficulty, category=selected_category)
    if not questions:
        print("No questions available. Please try again later.")
        return

    # Play the game
    score = 0
    for i, question in enumerate(questions, 1):
        choices = display_question(question, i)
        start_time = time.time()
        try:
            answer = int(input("Your answer (1-4): "))
            elapsed_time = time.time() - start_time
            if elapsed_time > time_limit:
                print("Time's up! The correct answer was:", question["correct_answer"])
                continue
            if choices[answer - 1] == question["correct_answer"]:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer was: {question['correct_answer']}")
        except (ValueError, IndexError):
            print(f"Invalid input! The correct answer was: {question['correct_answer']}")

    # Save the score and update stats
    save_score(player_name, score)
    update_player_stats(player_name, len(questions), score)

    # Display final score and leaderboard
    print(f"\nGame over! Your final score is: {score}/{num_questions}")
    display_leaderboard()

if __name__ == "__main__":
    play_game()