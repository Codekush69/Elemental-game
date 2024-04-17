import random
import tkinter as tk

# Function to play the game
def play_game(player_choice):
    elements = ["fire", "water", "earth"]
    computer_choice = random.choice(elements)

    result = ""
    if player_choice == computer_choice:
        result = "It's a tie"
    elif (player_choice == "fire" and computer_choice == "earth") or \
         (player_choice == "water" and computer_choice == "fire") or \
         (player_choice == "earth" and computer_choice == "water"):
        result = "You win!"
    else:
        result = "Computer wins!"
    
    computer_label.config(text="Computer's choice: " + computer_choice)
    result_label.config(text=result)

# Create main window
root = tk.Tk()
root.title("Elemental Game")

# Create buttons for player choices
fire_button = tk.Button(root, text="Fire", command=lambda: play_game("fire"))
fire_button.grid(row=0, column=0, padx=10, pady=10)

water_button = tk.Button(root, text="Water", command=lambda: play_game("water"))
water_button.grid(row=0, column=1, padx=10, pady=10)

earth_button = tk.Button(root, text="Earth", command=lambda: play_game("earth"))
earth_button.grid(row=0, column=2, padx=10, pady=10)

# Label to display computer's choice
computer_label = tk.Label(root, text="")
computer_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Label to display game result
result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Start the GUI main loop
root.mainloop()