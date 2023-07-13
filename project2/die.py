import stdio
import stdrandom

# Set value to a random integer from [1, 6].
value = stdrandom.uniformInt(1, 7)

# Set output to the empty string.
output = " "

# Set output to the appropriate string based on value.
if value == 1:
    output = "     \n  *  \n     "
elif value == 2:
    output = "*    \n     \n    *"
elif value == 3:
    output = "*    \n  *  \n    *"
elif value == 4:
    output = "*   *\n     \n*   *"
elif value == 5:
    output = "*   *\n  *  \n*   *"
elif value == 6:
    output = "*   *\n*   *\n*   *"
else:
    output = "Error"

# Write output to standard output.
stdio.writeln(output)
