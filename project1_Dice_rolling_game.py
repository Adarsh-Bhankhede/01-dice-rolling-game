
#! Dice Rolling Game --> week 1 - project 1

# Write a program that simulates rolling a pair of dice. Each time the program runs, it
# should randomly generate two numbers between 1 and 6 (inclusive), representing
# the result of each die. The program should then display the results and ask if the
# user would like to roll again.

#! Basic project: Program code

# import random

# while True:
#     choice = input("Rolling a Dices? (y/n): ").strip().lower()
#     if choice == 'y':
#         dice1 = random.randint(1,6)
#         dice2 = random.randint(1,6)
#         print(f" Dice: ({dice1},{dice2})")
#     elif choice == 'n':
#         print("Thank you for Playing !!!")
#         break
#     else:
#         print("Invalid Input!!!")

#! More Advanced version of Project: Program code

import random

dice_rolls_with_values = []
while True:
    choice = input("Rolling a Dices? (y/n): ").strip().lower()
    if choice == 'y': 
        no_of_dice = int(input("How many Dices want to Roll? : "))
        if no_of_dice <= 0:
            print("Invalid Input")
            continue
        
        record_dice_values = []
        for i in range(1, no_of_dice+1):
            dice = random.randint(1,6)
            record_dice_values.append(dice)
        print(f" Dice values: ",record_dice_values)
        dice_rolls_with_values.append(record_dice_values)
    
    elif choice == 'n':
        print("\n===Thank you for Playing !!!===")
        
        print("\n===== Record of Dice Roll =====\n")
        total_rolls = len(dice_rolls_with_values)
        print("Total Dice Throws : ",total_rolls)
        for i in range(total_rolls):
            print(f"Throw {i+1}. dice values: ",dice_rolls_with_values[i])
        break
    else:
        print("Invalid Input!!!")
