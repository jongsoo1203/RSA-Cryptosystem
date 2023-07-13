import stdio
import sys

# Accept m (int), d (int), and y (int) as command-line argument.
m = int(sys.argv[1])
d = int(sys.argv[2])
y = int(sys.argv[3])

# Set the calculation for dow.
y0 = y - (14 - m) // 12
x0 = y0 + y0//4 - y0 // 100 + y0 // 400
m0 = m + 12 * ((14 - m) // 12) - 2
dow = (d + x0 + 31 * m0 // 12) % 7

# Set output to the appropriate string based on value.
if dow == 0:
    output = "Sunday"
elif dow == 1:
    output = "Monday"
elif dow == 2:
    output = "Tuesday"
elif dow == 3:
    output = "Wednesday"
elif dow == 4:
    output = "Thursday"
elif dow == 5:
    output = "Friday"
else:
    output = "Saturday"

# Write output to standard output.
stdio.writeln(output)
