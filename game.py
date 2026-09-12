import tkinter as tk
from tkinter import messagebox
import random


class MemoryMatchGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Match")
        self.root.geometry("700x760")
        self.root.resizable(False, False)

        self.all_cards = [
            "A", "A", "B", "B", "C", "C",
            "D", "D", "E", "E", "F", "F",
            "G", "G", "H", "H"
        ]
        # Nested list
        self.round_cards = [
            self.all_cards[:6],    
            self.all_cards[:10],   
            self.all_cards[:16]    
        ]

        self.game_history = []
        self.leaderboard = []
        self.start_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def start_screen(self):
        self.clear_screen()

        title = tk.Label(
            self.root,
            text="MEMORY MATCH",
            font=("Arial", 30, "bold")
        )
        title.pack(pady=45)

        tk.Label(
            self.root,
            text="Match all the pairs before you run out of turns!",
            font=("Arial", 14)
        ).pack(pady=10)

        tk.Label(
            self.root,
            text="Enter your player name:",
            font=("Arial", 13)
        ).pack(pady=(35, 5))

        self.name_entry = tk.Entry(
            self.root,
            font=("Arial", 14),
            justify="center"
        )
        self.name_entry.pack()

        tk.Button(
            self.root,
            text="START GAME",
            font=("Arial", 14, "bold"),
            width=18,
            command=self.start_game
        ).pack(pady=25)

        tk.Button(
            self.root,
            text="HOW TO PLAY",
            font=("Arial", 12),
            width=18,
            command=self.show_instructions
        ).pack()

    def show_instructions(self):
        messagebox.showinfo(
            "How to Play",
            "1. Click two different cards.\n\n"
            "2. If they match, you earn a point.\n\n"
            "3. A wrong pair uses one turn.\n\n"
            "4. You can use PEEK twice each round.\n"
            "   Peek temporarily reveals all unmatched cards.\n"
            "   Peek also uses one turn.\n\n"
            "5. Complete all three rounds to win.\n\n"
            "6. Each round has more cards than the previous round."
        )

    def start_game(self):
        self.player_name = self.name_entry.get().strip()

        if self.player_name == "":
            messagebox.showwarning(
                "Missing Name",
                "Please enter your player name."
            )
            return

        self.score = 0
        self.current_round = 1
        self.game_history = []
        self.start_round()

    def start_round(self):
        self.clear_screen()

        # ---Select the current round's list using list indexing ^_____^
        self.cards = self.round_cards[self.current_round - 1].copy()
        random.shuffle(self.cards)

        # Lists controlling gameplay
        self.matched_cards = [False] * len(self.cards)
        self.revealed_cards = []
        self.matched_pairs = []
        self.turn_history = []

        self.first_choice = None
        self.second_choice = None
        self.busy = False

        self.turns = len(self.cards) + 2
        self.peek_uses = 2

        tk.Label(
            self.root,
            text=f"MEMORY MATCH - ROUND {self.current_round}",
            font=("Arial", 24, "bold")
        ).pack(pady=15)

        self.info_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 13)
        )
        self.info_label.pack()

        self.status_label = tk.Label(
            self.root,
            text="Choose two cards.",
            font=("Arial", 12)
        )
        self.status_label.pack(pady=8)

        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack(pady=15)

        self.buttons = []

        columns = 4

        for index in range(len(self.cards)):
            button = tk.Button(
                self.board_frame,
                text="?",
                font=("Arial", 18, "bold"),
                width=6,
                height=2,
                command=lambda i=index: self.choose_card(i)
            )
            button.grid(
                row=index // columns,
                column=index % columns,
                padx=7,
                pady=7
            )
            self.buttons.append(button)

        controls = tk.Frame(self.root)
        controls.pack(pady=10)

        self.peek_button = tk.Button(
            controls,
            text="PEEK",
            font=("Arial", 12, "bold"),
            width=12,
            command=self.use_peek
        )
        self.peek_button.grid(row=0, column=0, padx=8)

        tk.Button(
            controls,
            text="QUIT",
            font=("Arial", 12),
            width=12,
            command=self.quit_game
        ).grid(row=0, column=1, padx=8)

        self.update_info()

    def update_info(self):
        self.info_label.config(
            text=(
                f"Player: {self.player_name}    "
                f"Score: {self.score}    "
                f"Turns: {self.turns}    "
                f"Peek: {self.peek_uses}"
            )
        )

    def choose_card(self, index):
        if self.busy:
            return

        if self.matched_cards[index]:
            self.status_label.config(
                text="That card is already matched."
            )
            return

        if index in self.revealed_cards:
            self.status_label.config(
                text="Choose a different card."
            )
            return

        self.revealed_cards.append(index)
        self.buttons[index].config(text=self.cards[index])

        if self.first_choice is None:
            self.first_choice = index
            self.status_label.config(
                text="Now choose the second card."
            )
            return

        self.second_choice = index
        self.busy = True
        self.turns -= 1

        self.turn_history.append([
            self.first_choice + 1,
            self.second_choice + 1
        ])

        first = self.cards[self.first_choice]
        second = self.cards[self.second_choice]

        if first == second:
            self.handle_match()
        else:
            self.status_label.config(
                text=f"{first} and {second} do not match."
            )

            self.root.after(900, self.handle_mismatch)

    def handle_match(self):
        first = self.first_choice
        second = self.second_choice

        self.matched_cards[first] = True
        self.matched_cards[second] = True

        self.matched_pairs.append([
            self.cards[first],
            first + 1,
            second + 1
        ])

        self.score += 1

        self.buttons[first].config(state="disabled")
        self.buttons[second].config(state="disabled")

        if first in self.revealed_cards:
            self.revealed_cards.remove(first)
        if second in self.revealed_cards:
            self.revealed_cards.remove(second)

        self.status_label.config(text="MATCH!")

        self.first_choice = None
        self.second_choice = None
        self.busy = False

        self.update_info()
        self.check_round_end()

    def handle_mismatch(self):
        first = self.first_choice
        second = self.second_choice

        self.buttons[first].config(text="?")
        self.buttons[second].config(text="?")

        # Use pop() - remove revealed cards.
        # Pop by position safely from the end first.
        if len(self.revealed_cards) > 0:
            self.revealed_cards.pop()
        if len(self.revealed_cards) > 0:
            self.revealed_cards.pop()

        self.first_choice = None
        self.second_choice = None
        self.busy = False

        self.update_info()

        if self.turns <= 0:
            self.end_round(False)
        else:
            self.status_label.config(
                text="Try again. Choose two cards."
            )

    def use_peek(self):
        if self.busy:
            return

        if self.peek_uses <= 0:
            self.status_label.config(
                text="No Peek uses remaining this round."
            )
            return

        if self.first_choice is not None:
            self.status_label.config(
                text="Finish choosing the current pair first."
            )
            return

        if self.turns <= 0:
            return

        self.peek_uses -= 1
        self.turns -= 1
        self.busy = True

        self.revealed_cards = []

        for index in range(len(self.cards)):
            if not self.matched_cards[index]:
                self.revealed_cards.append(index)
                self.buttons[index].config(text=self.cards[index])

        self.status_label.config(
            text="PEEK! Remember the card positions..."
        )
        self.update_info()

        self.root.after(2500, self.hide_peek)

    def hide_peek(self):
        for index in self.revealed_cards:
            if not self.matched_cards[index]:
                self.buttons[index].config(text="?")

        # Clears Peek data using pop()
        while len(self.revealed_cards) > 0:
            self.revealed_cards.pop()

        self.busy = False

        if self.turns <= 0:
            self.end_round(False)
        else:
            self.status_label.config(
                text="Peek finished. Choose two cards."
            )

        self.update_info()

    def check_round_end(self):
        if len(self.matched_pairs) == len(self.cards) // 2:
            self.end_round(True)
        elif self.turns <= 0:
            self.end_round(False)

    def end_round(self, won):
        self.busy = True

        self.matched_pairs.sort()

        self.game_history.append({
            "round": self.current_round,
            "score": self.score,
            "turns_used": len(self.turn_history),
            "matched_pairs": self.matched_pairs.copy()
        })

        if won:
            if self.current_round < 3:
                messagebox.showinfo(
                    "Round Complete",
                    f"Great job, {self.player_name}!\n\n"
                    f"You completed Round {self.current_round}.\n"
                    f"Current score: {self.score}"
                )
                self.current_round += 1
                self.start_round()
            else:
                self.show_final_results(True)
        else:
            self.show_final_results(False)

    def show_final_results(self, won):
        self.clear_screen()

        title = "YOU WIN!" if won else "GAME OVER"

        tk.Label(
            self.root,
            text=title,
            font=("Arial", 28, "bold")
        ).pack(pady=25)

        tk.Label(
            self.root,
            text=f"Player: {self.player_name}",
            font=("Arial", 16)
        ).pack(pady=5)

        tk.Label(
            self.root,
            text=f"Final Score: {self.score}",
            font=("Arial", 18, "bold")
        ).pack(pady=5)

        self.leaderboard.append([self.player_name, self.score])

        # Sort the by score from highest to lowest.
        self.leaderboard.sort(key=lambda player: player[1], reverse=True)

        tk.Label(
            self.root,
            text="LEADERBOARD",
            font=("Arial", 16, "bold")
        ).pack(pady=(20, 5))

        leaderboard_text = ""
        for position in range(len(self.leaderboard)):
            player = self.leaderboard[position]
            leaderboard_text += (
                f"{position + 1}. {player[0]} - {player[1]} points\n"
            )

        tk.Label(
            self.root,
            text=leaderboard_text,
            font=("Arial", 11)
        ).pack()

        tk.Label(
            self.root,
            text="Search your name in the leaderboard:",
            font=("Arial", 12)
        ).pack(pady=(15, 5))

        self.search_entry = tk.Entry(
            self.root,
            font=("Arial", 13),
            justify="center"
        )
        self.search_entry.pack()

        tk.Button(
            self.root,
            text="SEARCH",
            font=("Arial", 11, "bold"),
            command=self.search_leaderboard
        ).pack(pady=8)

        self.search_result = tk.Label(
            self.root,
            text="",
            font=("Arial", 11)
        )
        self.search_result.pack(pady=3)

        tk.Button(
            self.root,
            text="PLAY AGAIN",
            font=("Arial", 13, "bold"),
            width=15,
            command=self.start_screen
        ).pack(pady=15)

        tk.Button(
            self.root,
            text="EXIT",
            font=("Arial", 12),
            width=15,
            command=self.quit_game
        ).pack()

    def search_leaderboard(self):
        search_name = self.search_entry.get().strip().lower()

        if search_name == "":
            self.search_result.config(
                text="Enter a player name to search."
            )
            return

        found = False

        for position in range(len(self.leaderboard)):
            player = self.leaderboard[position]

            if player[0].lower() == search_name:
                self.search_result.config(
                    text=(
                        f"Found {player[0]}! "
                        f"Rank #{position + 1} with {player[1]} points."
                    )
                )
                found = True
                break

        if not found:
            self.search_result.config(
                text=f"{search_name.title()} is not on the leaderboard yet."
            )

    def quit_game(self):
        if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
            self.root.destroy()


def main():
    root = tk.Tk()
    game = MemoryMatchGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
