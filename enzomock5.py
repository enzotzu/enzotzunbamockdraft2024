import pandas as pd
import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Define the draft rankings from the table
rankings = {
    'Vecenie': ['A. Sarr', 'R. Sheppard', 'S. Castle', 'D. Clingan', 'Z. Risacher', 'C. Williams', 'D. Carter', 'C. Carrington', 'D. Knecht', 'R. Holland', 'T. Salaun', 'M. Buzelis', 'N. Topic', 'J. McCain', 'R. Dillingham', 'K. Filipowski', 'Z. Edey', 'T. Da Silva', 'I. Collier', 'Y. Missi', 'T. Kolek', 'B. Scheierman', 'J. Walter', 'D. Holmes II', 'T. Smith', 'K. Ware', 'J. Furphy', 'J. Tyson', 'R. Dunn', 'A. Mitchell', 'J. Shead', 'A. Johnson', 'C. Christie', 'P. Dadiet', 'K. George', 'B. Klintman', 'N. Djurisic', 'C. Spencer', 'T. Shannon Jr.', 'A. Reeves'],
    'Givony': ['Z. Risacher', 'A. Sarr', 'D. Clingan', 'R. Sheppard', 'M. Buzelis', 'S. Castle', 'D. Knecht', 'R. Dillingham', 'T. Salaun', 'N. Topic', 'C. Williams', 'D. Carter', 'R. Holland', 'J. Walter', 'J. McCain', 'Z. Edey', 'T. Da Silva', 'J. Furphy', 'C. Carrington', 'K. George', 'K. Filipowski', 'Y. Missi', 'I. Collier', 'K. Ware', 'T. Kolek', 'B. Scheierman', 'R. Dunn', 'B. Klintman', 'P. Dadiet', 'J. Tyson', 'A. Johnson', 'J. Nunez', 'K. McCullar', 'D. Holmes II', 'J. Edwards', 'J. Mogbo'],
    'KOC': ['S. Castle', 'D. Clingan', 'M. Buzelis', 'R. Sheppard', 'D. Carter', 'T. Salaun', 'A. Sarr', 'Z. Risacher', 'D. Knecht', 'R. Dillingham', 'N. Topic', 'C. Williams', 'R. Holland', 'J. McCain', 'Z. Edey', 'J. Walter', 'C. Carrington', 'B. Klintman', 'I. Collier', 'K. Ware', 'T. Kolek', 'T. Da Silva', 'T. Shannon Jr.', 'N. Djurisic', 'Y. Missi', 'P. Dadiet', 'T. Smith', 'K. George', 'B. Scheierman', 'D. Holmes II', 'J. Tyson', 'R. Dunn', 'K. Filipowski', 'D. Holmes II', 'A. Bona', 'J. Mogbo', 'M. Ajinca'],
    'Yahoo': ['Z. Risacher', 'A. Sarr', 'D. Clingan', 'S. Castle', 'R. Sheppard', 'M. Buzelis', 'D. Knecht', 'C. Williams', 'T. Salaun', 'N. Topic', 'D. Carter', 'C. Carrington', 'R. Holland', 'J. Walter', 'J. McCain', 'R. Dillingham', 'K. George', 'Z. Edey', 'Y. Missi', 'T. Da Silva', 'I. Collier', 'T. Kolek', 'K. Ware', 'N. Djurisic', 'D. Holmes II', 'T. Shannon Jr.', 'P. Dadiet', 'J. Furphy', 'B. Scheierman', 'K. Filipowski', 'A. Johnson', 'C. Christie', 'J. Nunez', 'J. Tyson', 'R. Dunn', 'T. Smith', 'A. Johnson', 'T. Smith', 'D. Jones'],
    'NBAdraft.net': ['Z. Risacher', 'A. Sarr', 'R. Sheppard', 'C. Williams', 'S. Castle', 'M. Buzelis', 'T. Salaun', 'C. Carrington', 'D. Knecht', 'D. Clingan', 'R. Holland', 'J. Walter', 'J. McCain', 'Z. Edey', 'T. Da Silva', 'K. George', 'I. Collier', 'J. Tyson', 'T. Kolek', 'K. Ware', 'Y. Missi', 'R. Dillingham', 'N. Topic', 'P. Dadiet', 'T. Smith', 'P. Dadiet', 'J. Furphy', 'B. Klintman', 'A. Mitchell', 'R. Dunn', 'B. Klintman', 'J. Edwards', 'J. Mogbo', 'M. Ajinca', 'A. Johnson', 'A. Reeves'],
    'No Ceilings': ['A. Sarr', 'S. Castle', 'N. Topic', 'R. Sheppard', 'D. Clingan', 'Z. Risacher', 'D. Carter', 'M. Buzelis', 'C. Williams', 'R. Dillingham', 'D. Knecht', 'C. Carrington', 'T. Salaun', 'R. Holland', 'Z. Edey', 'J. McCain', 'T. Da Silva', 'J. Walter', 'K. Ware', 'K. Filipowski', 'T. Da Silva', 'Y. Missi', 'J. Furphy', 'T. Kolek', 'T. Smith', 'D. Holmes II', 'K. George', 'D. Jones', 'K. McCullar', 'H. Ingram', 'J. Tyson', 'C. Christie', 'A. Johnson', 'K. Simpson', 'J. Shead', 'R. Dunn', 'T. Alexander', 'D. Jones'],
    'Sporting News': ['A. Sarr', 'N. Topic', 'S. Castle', 'D. Knecht', 'Z. Risacher', 'R. Holland', 'T. Salaun', 'M. Buzelis', 'R. Dillingham', 'K. Filipowski', 'J. Walter', 'J. McCain', 'Z. Edey', 'T. Da Silva', 'C. Christie', 'K. George', 'T. Smith', 'J. Tyson', 'K. McCullar', 'K. Ware', 'J. Furphy', 'P. Dadiet', 'B. Scheierman', 'J. McCain', 'T. Alexander', 'T. Smith', 'J. Furphy', 'B. Klintman', 'K. McCullar', 'A. Johnson', 'A. Johnson', 'C. Christie', 'P. Dadiet', 'T. Alexander', 'J. Tyson', 'T. Shannon Jr.', 'A. Reeves'],
    'On3': ['A. Sarr', 'R. Sheppard', 'S. Castle', 'D. Clingan', 'Z. Risacher', 'R. Holland', 'T. Salaun', 'M. Buzelis', 'R. Dillingham', 'K. Filipowski', 'J. Walter', 'J. McCain', 'Z. Edey', 'T. Da Silva', 'C. Christie', 'K. George', 'T. Smith', 'J. Tyson', 'K. McCullar', 'K. Ware', 'J. Furphy', 'P. Dadiet', 'B. Scheierman', 'J. McCain', 'T. Alexander', 'T. Smith', 'J. Furphy', 'B. Klintman', 'K. McCullar', 'A. Johnson', 'A. Johnson', 'C. Christie', 'P. Dadiet', 'T. Alexander', 'J. Tyson', 'T. Shannon Jr.', 'A. Reeves'],
    'Alley Oop': ['A. Sarr', 'R. Holland', 'R. Sheppard', 'I. Collier', 'D. Carter', 'D. Holmes II', 'M. Buzelis', 'J. Tyson', 'K. Filipowski', 'J. Mogbo', 'D. Clingan', 'T. Da Silva', 'J. Furphy', 'B. Scheierman', 'Z. Risacher', 'T. Smith', 'D. Knecht', 'S. Castle', 'A. Bona', 'J. Shead', 'R. Dillingham', 'J. Wells', 'Z. Edey', 'K. McCullar', 'P. Dadiet', 'R. Dunn', 'C. Williams', 'T. Newton', 'I. Crawford', 'K. Simpson', 'J. McCain', 'N. Djurisic', 'N. Topic', 'D. Disu', 'J. Williams', 'H. Ingram', 'K. George', 'J. Ledee', 'M. Leons', 'C. Spencer'],
    'SBNation': ['N. Topic', 'A. Sarr', 'R. Holland', 'R. Sheppard', 'R. Dillingham', 'M. Buzelis', 'I. Collier', 'D. Clingan', 'D. Carter', 'S. Castle', 'Z. Risacher', 'T. Smith', 'K. Ware', 'C. Williams', 'T. Salaun', 'K. Filipowski', 'Y. Missi', 'D. Knecht', 'Z. Edey', 'J. McCain', 'D. Holmes II', 'J. Walter', 'J. Tyson', 'B. Carrington', 'T. Da Silva', 'P. Dadiet', 'K. McCullar', 'K. Simpson', 'J. Furphy', 'R. Dunn', 'T. Shannon Jr.', 'J. Shead', 'A. Bona', 'A. Mitchell', 'T. Kolek', 'K. George', 'N. Dante', 'B. Klintman', 'J. Mintz', 'J. Nunez', 'C. Spencer']
}

# Define the draft order
draft_order = [
    "Atlanta", "Washington", "Houston", "San Antonio", "Detroit", "Charlotte", "Portland", 
    "San Antonio", "Memphis", "Utah", "Chicago", "OKC", "Sacramento", "Portland", "Miami", 
    "Philadelphia", "LA Lakers", "Orlando", "Toronto", "Cleveland", "New Orleans", "Phoenix", 
    "Milwaukee", "New York", "New York", "Washington", "Minnesota", "Denver", "Utah", "Boston", 
    "Toronto", "Utah", "Milwaukee", "Portland", "San Antonio", "Indiana", "Minnesota"
]

# Function to perform the mock draft simulation
def start_mock_draft():
    draft_result = []
    selected_players = set()

    for idx, pick in enumerate(draft_order, 1):
        while True:
            source = random.choice(list(rankings.keys()))
            player = rankings[source][0]

            if player not in selected_players:
                draft_result.append((idx, pick, player))
                selected_players.add(player)
                for ranking in rankings.values():
                    if player in ranking:
                        ranking.remove(player)
                break

    df = pd.DataFrame(draft_result, columns=["Pick", "Team", "Player"])
    result_text = df.to_string(index=False)

    # Display the result in a new window
    result_window = tk.Toplevel(root)
    result_window.title("Mock Draft Result")
    result_label = tk.Label(result_window, text=result_text, justify=tk.LEFT, padx=10, pady=10)
    result_label.pack()

# Set up the tkinter window
root = tk.Tk()
root.title("Mock Draft Simulator")

# Load the basketball-themed image
image_path = "basketball.png"
img = Image.open(image_path)
img = img.resize((300, 300), Image.Resampling.LANCZOS)  # Adjust the size as needed
button_image = ImageTk.PhotoImage(img)

# Add a button to start the draft with the basketball image
start_button = tk.Button(root, image=button_image, command=start_mock_draft)
start_button.pack(pady=20)

# Run the tkinter main loop
root.mainloop()
