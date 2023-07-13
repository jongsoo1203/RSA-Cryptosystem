import stdio
import sys

# Accept x (int), y (int), and z (int) as command-line arguments.
x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

# Find the smallest value α and largest value ω using min() and max() functions.
a = min(x, y, z)
w = max(x, y, z)

# Find the middle value by subtracting min and max values from sum of all number
sum = x + y + z
mid = sum - a - w

# Write the numbers in ascending order, separated by a space.
stdio.writeln(str(a) + " " + str(mid) + " " + str(w))
