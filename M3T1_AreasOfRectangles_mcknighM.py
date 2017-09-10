# CTI110
# M3T1 - Areas of Rectangles
# Michael McKnight
# 09/10/2017

# This program is designed to measure the area of a rectangle, and which of
# two rectangles have the greater area.

# Get the dimensions of rectangle 1.
length1 = int(input("Enter the length of rectangle 1: "))
width1 = int(input("Enter the width of rectangle 1: "))

# Get the dimensions of rectangle 2.
length2 = int(input("Enter the length of rectangle 2: "))
width2 = int(input("Enter the width of rectangle 2: "))

# Calculate the areas of the rectangles.
area1 = length1 * width1
area2 = length2 * width2

# Determine which has the greater area.
if area1 > area2:
    print("Rectangle 1 has the greater area.")
elif area2 > area1:
    print("Rectangle 2 has the greater area.")
else:
    print("Both have the same area.")