# CTI110
# M6T2 - Feet to Inches
# Michael McKnight
# November 11, 2017

# This program converts feet to inches.

# Constant for the number of inches per foot.
INCHES_PER_FOOT = 12

# Main function.
def main():
    # Get a number of feet from the user.
    feet = int(input("Enter a number of feet: "))

    # Convert that to inches.
    print(feet, "ft. equals", feet_to_inches(feet), "inches.")

def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

# Call the main function.
main()
