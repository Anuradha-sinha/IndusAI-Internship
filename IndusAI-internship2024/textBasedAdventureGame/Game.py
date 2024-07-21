def start_game():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark forest. There are two paths ahead of you.")
    print("1. Take the left path")
    print("2. Take the right path")
    choice = input("Enter the number of your choice: ")
    if choice == "1":
        left_path()
    elif choice == "2":
        right_path()
    else:
        print("Invalid choice. Try again.")
        start_game()

def left_path():
    print("\nYou have taken the left path.")
    print("You encounter a river.")
    print("1. Try to swim across the river")
    print("2. Look for a bridge")
    choice = input("Enter the number of your choice: ")
    if choice == "1":
        print("The current is too strong, and you are swept away. Game over!")
    elif choice == "2":
        print("You find a bridge and cross safely. You win!")
    else:
        print("Invalid choice. Try again.")
        left_path()

def right_path():
    print("\nYou have taken the right path.")
    print("You find a small cabin.")
    print("1. Enter the cabin")
    print("2. Keep walking")
    choice = input("Enter the number of your choice: ")
    if choice == "1":
        print("You enter the cabin and find a treasure chest. You win!")
    elif choice == "2":
        print("You get lost in the forest and can't find your way out. Game over!")
    else:
        print("Invalid choice. Try again.")
        right_path()

# Start the game
start_game()
