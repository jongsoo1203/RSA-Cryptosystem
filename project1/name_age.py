import stdio
import sys

# Accept name (str) and age (str) as command-line arguments.
name = sys.argv[1]
age = sys.argv[2]

# Write the message "name is age years old." to standard output.
stdio.writeln(str(name) + " is " + str(age) + " years old.")
