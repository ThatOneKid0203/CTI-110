# CTI110
# M6T1 - Kilometer Converter
# Michael McKnight
# November 10, 2017

# This program converts an inputed amount of kilometers into miles.

CONVERSION_FACTOR = 0.6214

def main():
    # Get the distance in kilometers.
    kilometers = float(input("Enter a distance in kilometers: "))

    # Display the distance converted to miles.
    show_miles(kilometers)

def show_miles(km):
    # Calculate miles.
    miles = km * CONVERSION_FACTOR

    # Display the miles.
    print(km, "kilometers equals", miles, "miles.")

main()
