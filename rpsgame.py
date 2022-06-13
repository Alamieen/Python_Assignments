import random
print("YOU ARE WELCOME TO THE ROCK PAPER SCISSORS GAME")
user_wins = 0
computer_wins = 0



options = ['r', 'p', 's']

while True:
    user_input = input("\nType R to choose Rock\nP to choose Paper\nS to choose Scissors\nQ to quit The Game: ").lower()
    if  user_input == 'q':
         break
    if  user_input not in options:
         continue

    random_numb = random.randint(0,2)  
    cpu_pick = options[random_numb]  
   
    if user_input ==  'r' and cpu_pick == 'p':
        print("you won!")
       # print('you choose ')
        user_wins += 1
    elif user_input == 'p' and cpu_pick == 's':
        print('you won!')
        user_wins += 1
    elif user_input == 's' and cpu_pick == 'r':
        print('you won!')
        user_wins += 1
    else:
        print('You lost')
        computer_wins += 1    
print('You won', user_wins, 'times.')
print('Comuter won', computer_wins, 'times.') 
if user_wins > computer_wins:
    print("You are the winner💃")
elif user_wins < computer_wins:
    print("Computer wins 😋")
    print("Don't give up!!! \n\nPlay again.")
elif computer_wins == user_wins:
    print('Tie')
    print('You have an equal score .')

    
    