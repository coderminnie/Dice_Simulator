import random
import turtle as t

print('Welcome to Dice Simulator!')

def loading_results():
    
    for i in range(4):
        t.pensize(2)
        for c in ('blue', 'red', 'green'):
            t.color(c)
            t.forward(10)
            t.right(30)

    t.penup()
    t.left(180)
    t.forward(45)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.pendown()

    for steps in range(100, 103):
        for c in ('blue', 'red', 'green'):
            t.color(c)
            t.forward(steps)
            t.right(90)

def roll_unbiased_dice():
    result1=random.randint(1,6)
    print("Rolling a dice!")
    loading_results()
    print(f"Dice shows: {result1}")

def roll_biased_dice():
    list=[1,1,1,2,3,4,4,5,6,6,6,6,6,]
    result2=random.choice(list)
    print("Rolling a dice!")
    loading_results()
    print(f"Dice shows: {result2}")


decision=None
while (decision!=2) or (dice_type!=3):
    dice_type=int(input('''
    Select the type of dice:
    1. Unbiased Dice
    2. Biased Dice
        Or
    3. To exit the simulator

    '''))
    if(dice_type==3):
        print('\nExiting the Dice Simulator!\n')
        break

    decision=int(input('''
        Choose one option:
        1. Roll the dice
        2. Exit the simulator
                       
        '''
    ))
    print('\n')
    if(dice_type==1):
        
        if(decision==1):
            roll_unbiased_dice()
        elif(decision==2):
            print('Exiting the Dice Simulator!\n')
            break
        else:
            print('Enter the valid option!')

    elif(dice_type==2):
        if(decision==1):
            roll_biased_dice()
        elif(decision==2):
            print('Exiting the Dice Simulator!\n')
            break
        else:
            print('Enter the valid option!')
    else:
        print('Enter the valid option!')
