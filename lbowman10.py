#Lauren Bowman
#CTC386
# Lab 10
#GitHub test comment
def celsius():
    f = float(input( "What is the temperature in Fahrenheit?"))
    c =(f - 32) * 5/9
    print("The temperature in celsius is ", c)
#This is the main part of my program

name = input ("Hello, what's your name?")
print("Menu")
print("---------------")
print("Option 1")
print("Option 2")
print("Option 3")
print("Option 4")
print("Option 5")
print("Option 6")
print("----------------")
print("Hello,", name, ". Choose an option.")

correct = 10
jackpot = 2
option= int(input())

if (option==1):
         print ("How do you know when there's a singer at your door?")
         print ("They can't find the key and doesn't know when to come in!")
if (option==2):
    for i in range(15):
        print (name)
elif (option == 3):
    rep = int(input("Type a number 1-5."))
    for i in range (rep):
        print("You can't give your life more time, so give the time you have left more life.")

if (option == 4):

    x = int(input("Guess a number between 1 and 100: "))
    while (x != correct):

        while x < 1 or x >100:
            x = int(input("I'm sorry but you are out of range. Please select a number between 1 and 100: "))

        if x > correct:
            print ("You guessed too high, guess again!")
        elif x < correct:
            print ("You guessed too low, guess again!")

        x = int(input("Guess again: "))

    print("Woo hoo! You guessed the right number!")

if (option == 5):
    celsius()

if (option == 6):
    jackpot = 2

    while True:

        y = int(input("Congratuations!You won a prize! Choose box 1, box 2,or box 3. One box has a million dollars!"))

        while y < 1 or y > 3:
            y = int (input("I'm sorry, but choose a box numbered 1, 2, or 3."))

        if y == 1:
            print ("Congratulations! You won $1000!")
        elif y == 2:
            print ("Woot woot! You won the jackpot of $1,000,000!")
        elif y == 3:
            print ("Good choice! You won $10,000!")
        break




