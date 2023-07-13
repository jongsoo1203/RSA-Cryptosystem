import stdarray
import stdaudio
import stdio
import sys

# Read the waltz measures from standard input into a 1D list.
play = stdarray.create1D(32)
for i in range(32):
    play[i] = stdio.readInt()

# If the number of measures is not 32, exit with the message
if len(play) != 32:
    sys.exit("A waltz must contain exactly 32 measures")

# If a minuet measure is not from [1, 176], exit with the message
for i in range(0, 16):
    if play[i] > 176 or play[i] < 1:
        sys.exit("A minuet measure must be from [1, 176]")

# If a trio measure is not from [1, 96], exit with the message
for j in range(16, 32):
    if play[j] > 96 or play[j] < 1:
        sys.exit("A trio measure must be from [1, 96]")

# Play each of the first 16 minuet measures
for i in range(len(play)):
    if i <= 16:
        f = "data/M" + str(play[i])
        stdaudio.playFile(f)
    else:
        # Play each of the last 16 trio measures
        f = "data/T" + str(play[i])
        stdaudio.playFile(f)
