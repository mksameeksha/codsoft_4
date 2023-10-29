import random
import tkinter as tk

# Initialize scores
user_wins = 0
computer_wins = 0

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie"
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win"
    else:
        return "Computer wins"

# Function to update and display scores
def update_scores():
    user_score_label.config(text="User: " + str(user_wins))
    computer_score_label.config(text="Computer: " + str(computer_wins))

# Function to handle user's choice
def user_choice(choice):
    global user_wins, computer_wins
    computer_choice = random.choice(["rock", "paper", "scissors"])
    result = determine_winner(choice, computer_choice)
    
    if result == "You win":
        user_wins += 1
    elif result == "Computer wins":
        computer_wins += 1
    
    result_label.config(text="Result: " + result)
    user_choice_label.config(text="Your choice: " + choice)
    computer_choice_label.config(text="Computer's choice: " + computer_choice)
    update_scores()

# Create the main application window
app = tk.Tk()
app.geometry("700x450")
app.title("Rock-Paper-Scissors Game")

# Create and configure GUI components
rock_button = tk.Button(app, text="Rock", font=("arial", 20, "bold"), width=8, bg="#04364A", fg="#fff", bd=7, relief=tk.GROOVE, command=lambda: user_choice("rock"))
paper_button = tk.Button(app, text="Paper", font=("arial", 20, "bold"), width=8, bg="#04364A", fg="#fff", bd=7, relief=tk.GROOVE, command=lambda: user_choice("paper"))
scissors_button = tk.Button(app, text="Scissors", font=("arial", 20, "bold"), width=8, bg="#04364A", fg="#fff", bd=7, relief=tk.GROOVE, command=lambda: user_choice("scissors"))

result_label = tk.Label(app, text="Result: ", font=("arial", 20, "bold"), width=20, bg="#176B87", fg="#fff", bd=7, relief=tk.GROOVE)
user_choice_label = tk.Label(app, text="Your choice: ", font=("arial", 20, "bold"), width=20, bg="#64CCC5", fg="#fff", bd=7, relief=tk.GROOVE)
computer_choice_label = tk.Label(app, text="Computer's choice: ", font=("arial", 20, "bold"), width=22, bg="#176B87", fg="#fff", bd=7, relief=tk.GROOVE)

user_score_label = tk.Label(app, text="User: " + str(user_wins), font=("arial", 20, "bold"), width=7, bg="#04364A", fg="#fff", bd=7, relief=tk.GROOVE)
computer_score_label = tk.Label(app, text="Computer: " + str(computer_wins), font=("arial", 20, "bold"), width=10, bg="#04364A", fg="#fff", bd=7, relief=tk.GROOVE)

# Position GUI components using the grid manager
rock_button.grid(row=0, column=0, padx=20, pady=10)
paper_button.grid(row=0, column=1, padx=20, pady=10)
scissors_button.grid(row=0, column=2, padx=20, pady=10)

result_label.grid(row=1, column=0, columnspan=3, padx=20, pady=10)
user_choice_label.grid(row=2, column=0, columnspan=3, padx=20, pady=10)
computer_choice_label.grid(row=3, column=0, columnspan=3, padx=20, pady=10)
user_score_label.grid(row=4, column=0, padx=20, pady=10)
computer_score_label.grid(row=4, column=2, padx=20, pady=10)

# Start the GUI application
app.mainloop()
