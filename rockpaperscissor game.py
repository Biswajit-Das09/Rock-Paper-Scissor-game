import tkinter as tk
from tkinter import messagebox
import random

game_state = {
    'wins': 0,
    'losses': 0,
    'ties': 0,
    'player_name': ''
}

root = None
splash_screen = None

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        game_state['ties'] += 1
        return "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Scissors" and computer_choice == "Paper") or \
         (player_choice == "Paper" and computer_choice == "Rock"):
        game_state['wins'] += 1
        return "You win!"
    else:
        game_state['losses'] += 1
        return "You lose!"

def player_choice(choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    
    result = determine_winner(choice, computer_choice)
    
    result_text = f"Computer chose: {computer_choice}\n{result}"
    update_stats()
    result_label.config(text=result_text)

def update_stats():
    stats_text = (f"{game_state['player_name']}'s Stats:\n"
                  f"Wins: {game_state['wins']}\n"
                  f"Losses: {game_state['losses']}\n"
                  f"Ties: {game_state['ties']}")
    stats_label.config(text=stats_text)

def reset_game():
    game_state['wins'] = 0
    game_state['losses'] = 0
    game_state['ties'] = 0
    update_stats()
    result_label.config(text="")

def update_player_name():
    name = player_name_entry.get().strip()
    if name == "":
        messagebox.showwarning("Name Required", "Please enter a valid name.")
    else:
        game_state['player_name'] = name
        splash_screen.destroy()
        start_game()

def start_game():
    global root
    root = tk.Tk()
    root.title("Rock, Paper, Scissors Game")
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
    root.attributes('-fullscreen', True)
    create_game_ui()

def create_game_ui():
    global result_label, stats_label
    
    canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    canvas.pack(fill="both", expand=True)

    for i in range(root.winfo_screenheight()):
        color = f'#{int(255 - (i * 150 / root.winfo_screenheight())):02x}{int(150 + (i * 105 / root.winfo_screenheight())):02x}{int(255 - (i * 150 / root.winfo_screenheight())):02x}'
        canvas.create_line(0, i, root.winfo_screenwidth(), i, fill=color, width=1)

    frame = tk.Frame(root, bg="#ffffff", bd=10, relief="raised")
    frame.place(relx=0.5, rely=0.5, anchor="center", width=600, height=500)

    frame.grid_rowconfigure(0, weight=1)
    frame.grid_rowconfigure(1, weight=1)
    frame.grid_rowconfigure(2, weight=1)
    frame.grid_rowconfigure(3, weight=1)
    frame.grid_rowconfigure(4, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_columnconfigure(2, weight=1)

    title_label = tk.Label(frame, text="Rock, Paper, Scissors", font=("Arial", 24, "bold"),
                          bg="#ffffff", fg="#FF69B4")
    title_label.grid(row=0, column=0, columnspan=3, pady=15)

    global player_name_entry
    player_name_entry = tk.Entry(frame, font=("Arial", 14), bd=2, relief="groove")
    player_name_entry.insert(0, game_state['player_name'])
    player_name_entry.grid(row=1, column=0, columnspan=2, pady=10, sticky="ew")

    update_name_button = tk.Button(frame, text="Update Name", font=("Arial", 14), bg="#87CEFA", fg="white",
                                   relief="raised", command=update_player_name)
    update_name_button.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

    def create_button(text, emoji, color, command):
        button = tk.Button(frame, text=f"{emoji} {text}", font=("Arial", 16), bg=color, fg="white",
                           relief="raised", bd=5, command=command, padx=20, pady=10)
        return button

    create_button("Rock", "🪨", "#4CAF50", lambda: player_choice("Rock")).grid(row=2, column=0, padx=10, pady=10)
    create_button("Paper", "📜", "#2196F3", lambda: player_choice("Paper")).grid(row=2, column=1, padx=10, pady=10)
    create_button("Scissors", "✂️", "#F44336", lambda: player_choice("Scissors")).grid(row=2, column=2, padx=10, pady=10)

    global result_label
    result_label = tk.Label(frame, text="", font=("Arial", 16), bg="#ffffff")
    result_label.grid(row=3, column=0, columnspan=3, pady=10)

    global stats_label
    stats_label = tk.Label(frame, text="", font=("Arial", 14), bg="#ffffff")
    stats_label.grid(row=4, column=0, columnspan=3, pady=10)

    reset_button = tk.Button(frame, text="Reset Game", font=("Arial", 16), bg="#FF6347", fg="white",
                             relief="raised", command=reset_game)
    reset_button.grid(row=5, column=0, pady=10, sticky="ew")

    exit_button = tk.Button(frame, text="Exit", font=("Arial", 16), bg="#708090", fg="white",
                            relief="raised", command=root.destroy)
    exit_button.grid(row=5, column=2, pady=10, sticky="ew")

    update_stats()

def create_splash_screen():
    global splash_screen
    splash_screen = tk.Tk()
    splash_screen.title("Enter Your Name")

    splash_screen.geometry("400x200")

    splash_canvas = tk.Canvas(splash_screen, width=400, height=200, bg="#FFB6C1")
    splash_canvas.pack(fill="both", expand=True)

    splash_title_label = tk.Label(splash_screen, text="Welcome to Rock, Paper, Scissors", font=("Arial", 20, "bold"),
                                  bg="#FFB6C1", fg="#4682B4")
    splash_title_label.pack(pady=20)

    splash_name_frame = tk.Frame(splash_screen, bg="#FFB6C1")
    splash_name_frame.pack(pady=10)

    global player_name_entry
    player_name_entry = tk.Entry(splash_name_frame, font=("Arial", 14), bd=2, relief="groove")
    player_name_entry.insert(0, "Player")
    player_name_entry.pack(side="left", padx=5)

    start_button = tk.Button(splash_name_frame, text="Start Game", font=("Arial", 14), bg="#87CEFA", fg="white",
                            relief="raised", command=update_player_name)
    start_button.pack(side="left")

    splash_screen.mainloop()

create_splash_screen()
