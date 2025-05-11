import random
   
def main():
    print("Welcome to Coomber's Dice Rolling Game!") 

    while True:
        user_input = input("Do you want to roll the dice? (y/n): ").lower()
        if user_input == "y": 
            roll_1 = random.randint(1, 6)
            roll_2 = random.randint(1, 6)
            print(f"You rolled a: {roll_1} and {roll_2}")
        elif user_input == "n":
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


# Call the main function to start the game
if __name__ == "__main__":
    main()
    