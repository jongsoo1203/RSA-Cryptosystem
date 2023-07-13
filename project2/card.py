import stdio
import stdrandom

# Set the random ranks and suits for outcome
rank = stdrandom.uniformInt(2, 15)
suit = stdrandom.uniformInt(1, 5)

# Set output to the appropriate string based on value for rank.
if rank == 2:
    strrank = "2"
elif rank == 3:
    strrank = "3"
elif rank == 4:
    strrank = "4"
elif rank == 5:
    strrank = "5"
elif rank == 6:
    strrank = "6"
elif rank == 7:
    strrank = "7"
elif rank == 8:
    strrank = "8"
elif rank == 9:
    strrank = "9"
elif rank == 10:
    strrank = "10"
elif rank == 11:
    strrank = "Jack"
elif rank == 12:
    strrank = "Queen"
elif rank == 13:
    strrank = "King"
else:
    strrank = "Ace"

# Set output to the appropriate string based on value for suit.
if suit == 1:
    strsuit = "Clubs"
elif suit == 2:
    strsuit = "Diamonds"
elif suit == 3:
    strsuit = "Hearts"
else:
    strsuit = "Spades"

# Write the ranks and suits to standard output.
stdio.writeln(strrank + " of " + strsuit)
