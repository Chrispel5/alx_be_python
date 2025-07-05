from bank_account import BankAccount
import sys

def main():
    # Create a bank account object with some initial balance (e.g., 100)
    account = BankAccount(100)

    # Check if user passed a command
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Get the first argument and split it into command and value
    command_input = sys.argv[1]
    parts = command_input.split(":")
    command = parts[0]
    amount = float(parts[1]) if len(parts) > 1 else None

    # Handle the command
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        success = account.withdraw(amount)
        if success:
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
