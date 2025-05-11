import random
   
def main():
    print("Welcome to Coomber's Dice Rolling Game!") 

    while True:
        user_input = input("Do you want to roll the die? (y/n): ")
        if user_input == "y" or user_input == "Y":
            roll_1 = random.randint(1, 6)
            roll_2 = random.randint(1, 6)
            roll = roll_1 + roll_2
            print(f"You rolled a:{roll}!")
        elif user_input == "n" or user_input == "N":
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


# Call the main function to start the game
if __name__ == "__main__":
    main()
    