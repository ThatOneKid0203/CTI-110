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
