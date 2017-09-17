# CTI-110 
# M3HW1 - Age Classifier 
# Michael McKnight
# 09/17/2017

# This program asks for the person's age, and then tells them what they are.

# User inputs their age.
def main():
    age = int(input("What is your age?: "))

# Program gives description based on input.
    if age <= 1:
        print("You are an infant.")
    elif age >= 2 and age <= 12:
        print("You are a child.")
    elif age >= 13 and age <= 19:
        print("You are a teenager.")
    else:
        print("You are an adult.")

main()

