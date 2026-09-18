import math

# Get the coordinates of the two points from the user
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

# Calculate the differences between the x and y coordinates
print(math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)))

# Use the distance formula to find the distance between the points
distance = math.sqrt(x_difference**2 + y_difference**2)

# Display the calculated distance
print(distance)
