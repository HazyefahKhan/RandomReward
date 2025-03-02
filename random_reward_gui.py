import random
import tkinter as tk
from tkinter import messagebox, ttk
import sys

def roll_dice(num_dice=3, sides=20):
    """
    Roll a specified number of dice with a given number of sides.
    
    Args:
        num_dice (int): Number of dice to roll
        sides (int): Number of sides on each die
        
    Returns:
        list: Results of each die roll
    """
    results = [random.randint(1, sides) for _ in range(num_dice)]
    return results

def check_win(dice_results, win_threshold=15):
    """
    Check if all dice results are greater than or equal to the win threshold.
    
    Args:
        dice_results (list): List of dice roll results
        win_threshold (int): Minimum value required on each die to win
        
    Returns:
        bool: True if all dice are >= win_threshold, False otherwise
    """
    return all(result >= win_threshold for result in dice_results)

def calculate_sum(dice_results):
    """
    Calculate the sum of all dice results.
    
    Args:
        dice_results (list): List of dice roll results
        
    Returns:
        int: Sum of all dice results
    """
    return sum(dice_results)

def calculate_reward(dice_sum, paycheque_amount):
    """
    Calculate the reward amount based on the dice sum and paycheque amount.
    
    Args:
        dice_sum (int): Sum of dice results
        paycheque_amount (float): User's biweekly paycheque amount
        
    Returns:
        tuple: (multiplier, reward_amount)
    """
    # Define the reward tiers based on dice sum
    if 45 <= dice_sum <= 46:
        multiplier = 0.001
    elif 47 <= dice_sum <= 48:
        multiplier = 0.01
    elif 49 <= dice_sum <= 50:
        multiplier = 0.05
    elif 51 <= dice_sum <= 52:
        multiplier = 0.1
    elif 53 <= dice_sum <= 54:
        multiplier = 0.25
    elif 55 <= dice_sum <= 56:
        multiplier = 0.5
    elif 57 <= dice_sum <= 58:
        multiplier = 0.75
    elif 59 <= dice_sum <= 60:
        multiplier = 0.9
    else:
        # This should not happen with 3 dice all ≥ 15, but just in case
        multiplier = 0
    
    # Calculate the reward amount
    reward_amount = paycheque_amount * multiplier
    
    return (multiplier, reward_amount)

class RandomRewardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Reward Dice Roller")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        
        # Set default paycheque amount
        self.default_paycheque = 2500.00
        self.paycheque_amount = tk.DoubleVar(value=self.default_paycheque)
        
        # Create the main frame
        self.main_frame = ttk.Frame(root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create and place widgets
        self.create_widgets()
        
    def create_widgets(self):
        # Title
        title_label = ttk.Label(
            self.main_frame, 
            text="Random Reward Dice Roller", 
            font=("Arial", 18, "bold")
        )
        title_label.pack(pady=(0, 20))
        
        # Paycheque input frame
        paycheque_frame = ttk.Frame(self.main_frame)
        paycheque_frame.pack(fill=tk.X, pady=(0, 20))
        
        paycheque_label = ttk.Label(
            paycheque_frame, 
            text="Enter your biweekly paycheque amount: $",
            font=("Arial", 12)
        )
        paycheque_label.pack(side=tk.LEFT)
        
        paycheque_entry = ttk.Entry(
            paycheque_frame, 
            textvariable=self.paycheque_amount,
            width=10,
            font=("Arial", 12)
        )
        paycheque_entry.pack(side=tk.LEFT)
        
        # Instructions
        instructions_label = ttk.Label(
            self.main_frame,
            text="Click the button below to roll three 20-sided dice.\nYou win if all dice are ≥ 15!",
            font=("Arial", 12),
            justify=tk.CENTER
        )
        instructions_label.pack(pady=(0, 20))
        
        # Roll button
        self.roll_button = ttk.Button(
            self.main_frame,
            text="Roll for Reward",
            command=self.roll_for_reward,
            style="Roll.TButton"
        )
        self.roll_button.pack(pady=(0, 20))
        
        # Style for the roll button
        button_style = ttk.Style()
        button_style.configure("Roll.TButton", font=("Arial", 14, "bold"))
        
        # Results frame
        self.results_frame = ttk.LabelFrame(
            self.main_frame,
            text="Results",
            padding="10"
        )
        self.results_frame.pack(fill=tk.BOTH, expand=True)
        
        # Dice results
        self.dice_results_frame = ttk.Frame(self.results_frame)
        self.dice_results_frame.pack(fill=tk.X, pady=(10, 0))
        
        # Create labels for dice results
        self.dice_labels = []
        for i in range(3):
            dice_frame = ttk.Frame(self.dice_results_frame)
            dice_frame.pack(side=tk.LEFT, expand=True)
            
            dice_label = ttk.Label(
                dice_frame,
                text=f"Die {i+1}",
                font=("Arial", 12)
            )
            dice_label.pack()
            
            dice_value = ttk.Label(
                dice_frame,
                text="--",
                font=("Arial", 24, "bold")
            )
            dice_value.pack()
            
            self.dice_labels.append(dice_value)
        
        # Win/lose status
        self.status_label = ttk.Label(
            self.results_frame,
            text="Roll the dice to see if you win!",
            font=("Arial", 14),
            justify=tk.CENTER
        )
        self.status_label.pack(pady=(20, 0))
        
        # Reward calculation frame
        self.reward_frame = ttk.Frame(self.results_frame)
        self.reward_frame.pack(fill=tk.X, pady=(20, 0))
        
        # Sum label
        self.sum_label = ttk.Label(
            self.reward_frame,
            text="Sum: --",
            font=("Arial", 12)
        )
        self.sum_label.pack()
        
        # Multiplier label
        self.multiplier_label = ttk.Label(
            self.reward_frame,
            text="Multiplier: --",
            font=("Arial", 12)
        )
        self.multiplier_label.pack()
        
        # Reward label
        self.reward_label = ttk.Label(
            self.reward_frame,
            text="Reward: --",
            font=("Arial", 16, "bold")
        )
        self.reward_label.pack()
    
    def roll_for_reward(self):
        """Handle the roll button click event"""
        try:
            # Get paycheque amount
            paycheque = self.paycheque_amount.get()
            
            # Roll the dice
            dice_results = roll_dice(3, 20)
            
            # Update dice result labels
            for i, result in enumerate(dice_results):
                self.dice_labels[i].config(text=str(result))
            
            # Check win condition
            if check_win(dice_results):
                # Calculate sum
                dice_sum = calculate_sum(dice_results)
                
                # Calculate reward
                multiplier, reward = calculate_reward(dice_sum, paycheque)
                
                # Update status label with win message
                self.status_label.config(
                    text="🎉 Congratulations! You WON! 🎉",
                    foreground="green"
                )
                
                # Update reward calculation labels
                self.sum_label.config(text=f"Sum: {dice_sum}")
                self.multiplier_label.config(text=f"Multiplier: {multiplier:.3f}")
                self.reward_label.config(text=f"Reward: ${reward:.2f}")
                
                # Make reward frame visible
                self.reward_frame.pack(fill=tk.X, pady=(20, 0))
            else:
                # Update status label with lose message
                self.status_label.config(
                    text="😞 Sorry, you lost. Not all dice are ≥ 15.",
                    foreground="red"
                )
                
                # Reset reward calculation labels
                self.sum_label.config(text="Sum: --")
                self.multiplier_label.config(text="Multiplier: --")
                self.reward_label.config(text="Reward: --")
        
        except ValueError:
            # Handle invalid paycheque amount
            messagebox.showerror(
                "Invalid Input",
                "Please enter a valid number for your paycheque amount."
            )
            self.paycheque_amount.set(self.default_paycheque)

def main():
    root = tk.Tk()
    app = RandomRewardApp(root)
    root.mainloop()

if __name__ == "__main__":
    main() 