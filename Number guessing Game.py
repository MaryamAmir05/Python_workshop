#number guessing game
import random
num = random.randint(1,10)
is_true = False
while is_true == False:
    ask = int(input("Enter a number: "))
    if ask == num:
        print("Correct Guess!")
        is_true = True
    elif ask > num:
        print("Too high")
    elif ask < num:
        print("Too low")