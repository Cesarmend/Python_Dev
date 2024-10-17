# Python Slot Machine


def spin_row():
    pass

def print_row():
    pass

def get_payout():
    pass

def main():
    balance = 100

    print("**************************")
    print("Welcome to Python Slots")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("**************************")

    while balance>0 :
        print(f"Current balance: $ {balance}")

        bet = input("place your bet amount: ")

        if not bet.isdigit():
            
            print("Please enter a valid number")
            print("---------------------------")
            continue

        bet = int(bet)

        if bet> balance:
            print("Insuficient funds")
            print("---------------------------")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet 

        row = spin_row()
        pass

if __name__ == '__main__': 
    main()