#Lauren Bowman
#Final Exam
#Question 1

print ("option 1")
print ("option 2")
print ("option 3")
print ("---------------")

print ("Hello, please pick an option")
x = int(input())

if (x ==1):
    n = input ("Hello, what's your name?")
    print ("Hello,",n ,"why did you have problems riding the motorcycle?")
    print ("Because you forgot to flip the killswitch!")

if (x==2):
    for i in range (20):
        print("cheesecake")

if (x==3):
    y = int(input("Please pick a number between 0 and 5"))
    while y != 0:
        if y < 0 or y > 5:
            y = int(input ("Out of range, try again: "))
        else:
            y = int(input ("You're in range, but I want zero: ")) 
    print("Great job, you have zeroed out.")


