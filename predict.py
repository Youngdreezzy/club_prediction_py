# Dashboard
# User NAme input
# 


club = [ 'Chelsea',
         'Arsenal',
         'Liverpool',
         'Aston Villa',
         'Brighton',
         'Tottenham',
         'Newcastle',
         'Fullham',
         'Man United',
         'Man City'
        ]
import random
predict = random.choice(club)
information = []





def dashboard():
    print(
        '''
        *** Welcome to Club Prediction App ***

        1. Sign up
        2. Play Game
        3. View Result
        #. Exit

        '''
        )
    option = input('Option: ')
    if option == '1':
        info()
    elif option == '2':
        game()

def info():
    global information
    surname = input('Enter your surname: ')
    first_name = input('Enter your firstname: ')
    phone_num = int(input('Enter your mobile number: '))
    age = int(input('Age: '))
    information = (f"Fullname => {surname} {first_name},\n Mobile No => {phone_num},\n Age => {age}")
    if age < 18:
        print("You're under age, Stop! playing bet")
        return
    else:
        print(f'\n*** Welcome {first_name} ***')

    print(f'Kindly check if your information is correct:\n {information}')
    route = input(' Press 1 to input information again or enter to continue: ')
    if route == '1':
        info()
    else:
        dashboard()



def game():
    global club, predict
    if not information:
        print("Please sign up before playing the game.")
        dashboard()
        return

    print('Welcome to Premier League Winner Prediction')
    print(club)
    option = input('Kindly Predict the club that will win the league: ')
    

    if option.strip() != predict:
        prog = input('* What is cashout * \nPress 1 to exit or enter to try again')
        if prog == '1':
            exit()
        else:
            game()
    else:
        print("*** Hurray!! You've won 10 Million US Dollars ***\n" * 7)
        return  
    ### Or create option for account balance and display balance



dashboard()





