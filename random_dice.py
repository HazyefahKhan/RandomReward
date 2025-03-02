import random
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

def main():
    """Main function to run the dice rolling program."""
    # Default biweekly paycheque amount
    default_paycheque = 2500.00
    
    print("Welcome to the Dice Roller!")
    
    # Parse command line arguments
    if len(sys.argv) > 1:
        try:
            paycheque_amount = float(sys.argv[1])
            print(f"Using paycheque amount from command line: ${paycheque_amount:.2f}")
        except ValueError:
            print(f"Invalid command-line argument. Using default amount: ${default_paycheque:.2f}")
            paycheque_amount = default_paycheque
    else:
        # Allow user to customize paycheque amount via input
        try:
            user_input = input(f"Enter your biweekly paycheque amount (default: ${default_paycheque:.2f}): ")
            if user_input.strip():
                paycheque_amount = float(user_input)
            else:
                paycheque_amount = default_paycheque
        except ValueError:
            print(f"Invalid input. Using default amount: ${default_paycheque:.2f}")
            paycheque_amount = default_paycheque
    
    print(f"\nUsing paycheque amount: ${paycheque_amount:.2f}")
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
        # Calculate and display sum only if user won
        dice_sum = calculate_sum(dice_results)
        print("\n🎉 Congratulations! You WON! All dice are ≥ 15. 🎉")
        print(f"The sum of your dice is: {dice_sum}")
        
        # Calculate and display reward
        multiplier, reward = calculate_reward(dice_sum, paycheque_amount)
        print(f"\nReward Calculation:")
        print(f"Dice Sum: {dice_sum} → Multiplier: {multiplier:.3f}")
        print(f"Reward: ${paycheque_amount:.2f} × {multiplier:.3f} = ${reward:.2f}")
    else:
        print("\n😞 Sorry, you lost. Not all dice are ≥ 15.")
    
    print("\nThank you for using the Dice Roller!")

if __name__ == "__main__":
    main() 