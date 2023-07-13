import stdarray
import stdrandom
import stdio

# Read the minuet measures from standard input into a 2D list with dimensions 11 × 16.
minuet = stdarray.create2D(11, 16)

# store every element into the list.
for i in range(0, 11):
    for j in range(0, 16):
        minuet[i][j] = stdio.readInt()

# Set minuet dierolls in range[0,5] for the ranmdom two numbers.
# Thus, later, when list is reading the row, it will start with 0 which is the 1st element of list.
mdie1 = stdrandom.uniformInt(0, 6)
mdie2 = stdrandom.uniformInt(0, 6)

# Write to standard output a random sequence of 16 minuet measures.
# Set for loop to make the random 16 measure
for j in range(0, 16):
    # Set the row value as the sum of die rolls
    stdio.write(str(minuet[mdie1 + mdie2][j]) + ' ')

# Read the trio measures from standard input into a 2D list with dimensions 6 × 16.
Trio = stdarray.create2D(6, 16)

# store every element into the list.
for i in range(0, 6):
    for j in range(0, 16):
        Trio[i][j] = stdio.readInt()

# Set the die for random die number.
triodie = stdrandom.uniformInt(0, 6)

# Write to standard output a random sequence of 16 trio measures
# Set for loop to make the random 16 measure
for j in range(0, 16):
    stdio.write(str(Trio[triodie][j]) + ' ')
# since all 32 elements are written, end the output.
stdio.writeln()
