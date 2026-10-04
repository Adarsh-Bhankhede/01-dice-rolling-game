
# 🎲 Dice Rolling Game

**Week 1 - Project 1**

## Description

Write a Python program that simulates rolling a pair of dice.

Each time the program runs, it should randomly generate **two numbers between 1 and 6 (inclusive)**, representing the result of each die.

The program should then display the results and ask the user if they would like to roll again.

## Optional Enhancements

* Modify the program so the user can specify **how many dice** they want to roll.
* Add a feature to keep track of **how many times the user has rolled the dice** during the session. This requires a counter that increments each time the dice are rolled.

## Program Flow

```text
1. Start the program.
2. Ask the user if they want to roll the dice.
3. If the user enters "y":
   - Generate two random numbers between 1 and 6.
   - Display the result of both dice.
   - Increment the roll counter.
   - Ask the user if they want to roll again.
4. If the user enters "n":
   - Display a thank-you message.
   - Exit the program.
5. If the user enters any other character:
   - Display an "Invalid input" message.
   - Ask the user again.
```

## Concepts Used

* `while` loop
* `if-elif-else`
* `input()`
* `random.randint()`
* Variables
* Counter
