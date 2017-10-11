# CTI110
# M5T2 - Bug Collector
# Michael McKnight
# October 11, 2017

# This program is designed to show how many bugs one has collected over a week.

def main():
    # Initialize the accumulator.
    total = 0

    # Get the bugs collected for each day.
    for day in range(1,8):
        # Prompt the user.
        print("Enter the bugs collected for day", day)

        # Input the number of bugs.
        bugs = int(input())

        # Add bugs to total.
        total += bugs
        
    # Display the total bugs.
    print("You collect a total of", total, "bugs.")
main()
