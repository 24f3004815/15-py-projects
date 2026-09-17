import random 

U_score = 0
C_score = 0

while True:
    user = int(input("Enter the number between 1 to 5: \n"))
    comp = random.randint(1,5)

    if user == comp:
        print("Tie \n")

    elif user > comp:
        print('You won \n')
        U_score += 1 

    elif user < comp:
        print('Computer won \n')
        C_score += 1 

    else:
        print('Invalid input \n')

    print('Your score:',U_score , '\n Computer Score:' , C_score)

    ask = input("Do you want to continue y/n :\n")

    if ask.lower() == 'n':
        break 

    