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

def main():
    """Main function to run the dice rolling program."""
    print("Welcome to the Dice Roller!")
    print("Rolling three 20-sided dice...")
    
    # Roll three 20-sided dice
    dice_results = roll_dice(3, 20)
    
    # Display the results
    print("\nYour dice results:")
    for i, result in enumerate(dice_results, 1):
        print(f"Die {i}: {result}")
    
    print("\nThank you for using the Dice Roller!")

if __name__ == "__main__":
    main() 