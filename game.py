import random

class TextAdventureGame:
    def __init__(self):
        self.player_name = ""
        self.player_energy = 100
        self.player_score = 0
        self.current_location = "village"
        self.inventory = [] 
        
        self._score_threshold = 50

    def start_game(self):
        print("Welcome to the Data Academy Text Adventure!")
        self.player_name = input("What's your name, adventurer? ")
        print(f"Welcome, {self.player_name}! Your adventure begins in a small village.")
        self.game_loop()

    def game_loop(self):
        while True:
            print(f"\nYou are in the {self.current_location}.")

            action = input("What would you like to do? (explore/rest/use item/quit): ").lower()

            if action == "explore":
                self.explore()
            elif action == "rest":
                self.rest()
            elif action == "use item":
                self.use_item()
            elif action == "quit":
                print("Thanks for playing!")
                break
            else:
                print("Invalid action. Try again.")

    def explore(self):
        events = [
            "You find a small treasure!",
            "You encounter a friendly traveler.",
            "You discover a hidden path.",
            "You find a energy potion!",
            "You find a mysterious map!"
        ]
        event = random.choice(events)
        print(event)
        
        self.player_energy -= 20
        self.player_score += 5
        print(f"Your energy is now {self.player_energy}")

    def rest(self):
        self.player_energy += 20
        if self.player_energy > 100:
            self.player_energy = 100
        print(f"You rest and recover. Your energy is now {self.player_energy}")

    def use_item(self):
        if not self.inventory:
            print("Your inventory is empty!")
            return
        
        print("Your inventory:")
        for i, item in enumerate(self.inventory, 1):
            print(f"{i}. {item}")
        
        choice = input("Enter the number of the item you want to use (or 'cancel'): ")
        if choice.lower() == 'cancel':
            return

if __name__ == "__main__":
    game = TextAdventureGame()
    game.start_game()