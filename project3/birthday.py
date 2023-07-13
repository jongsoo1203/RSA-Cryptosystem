import stdarray
import stdio
import stdrandom
import sys

DAYS_PER_YEAR = 365

# Accept trials (int) as command-line argument.
trials = int(sys.argv[1])

# Set count, denoting the total number of individuals sampled across the trials number of
# experiments, to 0.
count = 0

for i in range(0, trials + 1):
    # Perform trials number of experiments, where each experiment involves sampling individuals
    # until a pair of them share a birthday...

    # Setup a 1D list birthdaysSeen of DAYS_PER_YEAR booleans, all set to False by default. This
    # list will keep track of the birthdays encountered in this experiment.
    birthdaysSeen = stdarray.create1D(DAYS_PER_YEAR, False)

    while True:
        # Sample individuals until match...

        # Increment count by 1.
        count += 1

        # Set birthday to a random integer from [0, DAYS_PER_YEAR).
        birthday = stdrandom.uniformInt(0, DAYS_PER_YEAR)

        if birthdaysSeen[birthday]:
            # If birthday has been encountered, abort this experiment, ie, break.
            break
        else:
            # Record the fact that we are seeing this birthday for the first time.
            birthdaysSeen[birthday] = True

# Write to standard output the average number of people that must be sampled before a match,
# as an int.
stdio.writeln(count // trials)
