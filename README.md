# RandomReward

A simple Python program that simulates rolling dice with win conditions and rewards.

## Current Features

- Rolls three 20-sided dice (d20)
- Displays the results of each die roll
- Determines if the user won based on a win condition
- Win condition: All three dice must be ≥ 15
- Calculates and displays the sum of dice rolls when the user wins
- Maps dice sum to reward amount based on a customizable paycheque value
- Simple GUI interface with a "Roll for Reward" button

## Reward System

The program calculates rewards based on the sum of dice and the user's biweekly paycheque:

| Sum of Dice | Multiplier | Reward Calculation Example (with $2500 paycheque) |
|-------------|------------|---------------------------------------------------|
| 45-46       | 0.001      | $2500 × 0.001 = $2.50                             |
| 47-48       | 0.01       | $2500 × 0.01 = $25.00                             |
| 49-50       | 0.05       | $2500 × 0.05 = $125.00                            |
| 51-52       | 0.1        | $2500 × 0.1 = $250.00                             |
| 53-54       | 0.25       | $2500 × 0.25 = $625.00                            |
| 55-56       | 0.5        | $2500 × 0.5 = $1,250.00                           |
| 57-58       | 0.75       | $2500 × 0.75 = $1,875.00                          |
| 59-60       | 0.9        | $2500 × 0.9 = $2,250.00                           |

## How to Run

### Command Line Version

1. Make sure you have Python installed on your system
2. Run the program using one of these methods:
   ```
   # Interactive mode (will prompt for paycheque amount)
   python random_dice.py
   
   # Command-line mode (specify paycheque amount directly)
   python random_dice.py 3000
   ```
3. If using interactive mode, enter your biweekly paycheque amount when prompted (or press Enter to use the default $2500)

### GUI Version

1. Make sure you have Python installed on your system
2. Run the GUI version using:
   ```
   python random_reward_gui.py
   ```
3. Enter your biweekly paycheque amount in the input field
4. Click the "Roll for Reward" button to roll the dice and see your results

## Requirements

- Python 3.6 or higher
- Tkinter (included in standard Python installations) for the GUI version
- No external dependencies required
