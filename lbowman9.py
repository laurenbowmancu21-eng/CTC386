#Lauren Bowman
#Lab 9
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
print("----------------")
print("Hello,", name, ". Choose an option.")

correct = 10

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

