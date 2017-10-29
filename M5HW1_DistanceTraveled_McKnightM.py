# CTI110
# M5HW1 - Distance Traveled
# Michael McKnight
# October 29, 2017

# This program tells the distance traveled at a certain speed over a specific
# time in hours.

def main():
    
    # First, the speed inputed.
    speed = int(input("What speed was the vehicle traveling in MPH?: "))

    # Next, the time traveled.
    hours = int(input("How many hours did it take?: "))
    
    print("Hours \t Distance")
    print("---------------------")

    # Now it calculates the distance.
    for time in range(1, 1 + hours):
        distance = speed * time
        print(time, "\t", distance, "miles")

main()
