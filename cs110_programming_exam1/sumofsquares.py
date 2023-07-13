import stdio

# Read ints
x = stdio.readAllInts()

Sum = 0
# sum of every square
for i in range(len(x)):
    Sum += x[i] ** 2

# Write the standerd output
stdio.writeln(Sum)
