# CTI-110 
# M2HW2 - Tip Tax Total 
# Michael McKnight
# 09/10/2017

# This program is designed to calculate the total cost of a meal, including tip,
# at 18% and a 7% sales tax

# First, the user inputs to cost.
foodCost = float(input ("Enter the cost of meal: $"))

# Next, the program calculates the tip.
tipPercentage = 0.18 * foodCost

# Then the sales tax.
salesTax = 0.07 * foodCost

# Finally it's all calculated together.
total = foodCost + tipPercentage + salesTax

print ("Meal cost: $", format(foodCost, ",.2f"), "Tip: ","%", \
       format(tipPercentage, ",.2f"), "Sales tax: ","%", format(salesTax, ",.2f")\
       , "Total Cost: $", format(total, ",.2f"))
