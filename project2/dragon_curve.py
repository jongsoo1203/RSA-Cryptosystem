import stdio
import sys

# Accept n (int) as command-line argument.
n = int(sys.argv[1])

# Set dragon and nogard to the string “F”.
dragon = nodgard = "F"

# Repeat i for each [1, n]
for i in range(1, n+1):
    # Exchange dragon and nogard with dragon “L” nogard and dragon “R” nogard
    dragon, nodgard = dragon + "L" + nodgard, dragon + "R" + nodgard

# Write dragon (dragon curve of order n) as standard output.
stdio.writeln(dragon)
