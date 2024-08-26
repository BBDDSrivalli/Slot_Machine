
import random

# Constants
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

# Define the check_winning function
def check_winning(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:  # Only executed if the loop didn't break
            winnings += values[symbol] * bet
            winning_lines.append(line + 1) 
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column) 
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, col in enumerate(columns):
            if i != len(columns) - 1:
                print(col[row], end=" | ")
            else:
                print(col[row], end="")
        print()

# Function to handle user deposit
def deposit():
    while True:
        amount = input("How much would you like to deposit? ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Enter a positive number!")
        else:
            print("Enter numbers only!")
    return amount

# Function to get the number of lines to bet on
def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1 - {MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Enter a number between 1 and {MAX_LINES}!")
        else:
            print("Enter numbers only!")
    return lines

# Function to get the bet amount per line
def get_bet():
    while True:
        amount = input(f"How much would you like to bet on each line? (Minimum: {MIN_BET}, Maximum: {MAX_BET}) ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"The bet amount should be between {MIN_BET} and {MAX_BET} rupees.")
        else:
            print("Enter numbers only!")
    return amount


def spin(balance):
    lines = get_number_of_lines()
    
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print("You don't have enough balance to make this bet.")
            print(f"Your current balance is {balance} rupees.")
        else:
            break

    print(f"You are betting {bet} rupees on each of the {lines} lines. Total bet amount: {total_bet} rupees.")
    balance -= total_bet  # Update balance after the bet
    print(f"Balance after bet: {balance} rupees.")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winning(slots, lines, bet, symbol_count)
    print(f"You won {winnings} rupees")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

# Main function to manage the betting process
def main():
    balance = deposit()
    while True:
        print(f"Current balance is {balance} rupees")
        ans = input("Press enter to play or 'q' to quit: ")
        if ans == "q":
            break
        balance += spin(balance)
    print(f"You are left with {balance} rupees.")

# Call the main function to run the program
main()
