# CTI-110 
# M3HW2 - Software Sales 
# Michael McKnight
# 09/17/2017

# This program asks for number of packages purchased, and gives the discount and
# total purchase cost.

# User inputs a value over ten, and calculates total raw cost.
def main():
    quantity = int(input("How many packages did you purchase?: "))
    initialTotal = quantity * 99

# Program then calculates and displays the total with discount.
    if quantity >= 10 and quantity <= 19:
        discount = initialTotal * .10
        total = initialTotal - discount
        print("If you buy {} packages, your discount is ${} and your total is ${}."\
              .format(quantity, discount, total))

    elif quantity >= 20 and quantity <= 49:
         discount = initialTotal * .20
         total = initialTotal - discount
         print("If you buy {} packages, your discount is ${} and your total is ${}."\
               .format(quantity, discount, total))

    elif quantity >= 50 and quantity <= 99:
         discount = initialTotal * .30
         total = initialTotal - discount
         print("If you buy {} packages, your discount is ${} and your total is ${}."\
               .format(quantity, discount, total))
    else:
         discount = initialTotal * .40
         total = initialTotal - discount
         print("If you buy {} packages, your discount is ${} and your total is ${}."\
               .format(quantity, discount, total))
main()
