import random

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

def main():
    """Main function to run the dice rolling program."""
    print("Welcome to the Dice Roller!")
    print("Rolling three 20-sided dice...")
    print("Win condition: All three dice must be ≥ 15")
    
    # Roll three 20-sided dice
    dice_results = roll_dice(3, 20)
    
    # Display the results
    print("\nYour dice results:")
    for i, result in enumerate(dice_results, 1):
        print(f"Die {i}: {result}")
    
    # Check win condition and display result
    if check_win(dice_results):
        print("\n🎉 Congratulations! You WON! All dice are ≥ 15. 🎉")
    else:
        print("\n😞 Sorry, you lost. Not all dice are ≥ 15.")
    
    print("\nThank you for using the Dice Roller!")

if __name__ == "__main__":
    main() 