import random

club = [
    'Chelsea', 
    'Arsenal', 
    'Liverpool', 
    'Aston Villa', 
    'Brighton',
    'Tottenham', 
    'Newcastle', 
    'Fulham', 
    'Man United', 
    'Man City'
]

user_info = {}
game_results = []

def dashboard():
    print(
        '''
        *** Welcome to Club Prediction App ***

        1. Sign Up
        2. Play Game
        3. View Result
        4. Exit
        '''
    )
    option = input('Select an option: ')
    if option == '1':
        info()
    elif option == '2':
        game()
    elif option == '3':
        view_result()
    elif option == '4':
        print("Thank you for playing! Exiting...")
        exit()
    else:
        print("Invalid option. Please try again.")
        dashboard()

def get_phone_number():
    phone_num = input('Enter your mobile number: ')
    while phone_num.isdigit() == False:
        print("Invalid number. Please enter digits only.")
        phone_num = input('Enter your mobile number: ')
    return int(phone_num)

def get_age():
    age = input('Enter your age: ')
    while age.isdigit() == False or int(age) <= 0:
        print("Invalid input. Please enter a valid age.")
        age = input('Enter your age: ')
    return int(age)

def info():
    print("Please provide your information:")
    surname = input('Enter your surname: ')
    first_name = input('Enter your first name: ')
    
    phone_num = get_phone_number()
    age = get_age()

    if age < 18:
        print("You're underage and cannot play the game.")
        return
    else:
        global user_info
        user_info = {
            'surname': surname,
            'first_name': first_name,
            'phone_num': phone_num,
            'age': age
        }
        print(f'\n*** Welcome, {first_name}! ***')
        print(f"Your information: {user_info}")
        route = input('Press 1 to re-enter information or any other key to continue: ')
        if route == '1':
            info()
        else:
            dashboard()


def game():
    global club, game_results
    predict = random.choice(club)

    if not user_info:
        print("!!! Please sign up before playing the game !!!")
        dashboard()
        return
    
    print('\nWelcome to Premier League Winner Prediction')
    print("Clubs:", ", ".join(club))
    
    option = input('Predict the club that will win the league: ').strip().title()

    if option not in club:
        print("Invalid club name. Please select a club from the list.")
        return game()

    if option == predict:
        print("*** Hurray!! You've won 10 Million US Dollars! ***\n" * 3)
        result = "Win"
    else:
        print("Sorry, that was incorrect. Try again!")
        result = "Lose"

    game_results.append((option, predict, result))
    
    prog = input('Press 1 to return to the dashboard or any other key to play again: ')
    if prog == '1':
        dashboard()
    else:
        game()


def view_result():
    if not game_results:
        print("No game results to display. Play the game first!")
    else:
        print("\n--- Game Results ---")
        index = 1
        for user_guess, actual, outcome in game_results:
            print(f"{index}. You guessed: {user_guess} | Actual winner: {actual} | Result: {outcome}")
            index += 1
    input("\nPress Enter to return to the dashboard.")
    dashboard()


def main():
    dashboard()


# Run the main function to start the game
main()
