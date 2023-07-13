import stdio
import sys

# Accept t (float) and v (float) as command-line argument.
t = float(sys.argv[1])
v = float(sys.argv[2])

# if statement to decide when to report the error messages and when to compute.
# For the temperature error.
if t > 50:
    stdio.writeln("Value of t must be <= 50 F")
else:
    w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * v**0.16
    # For the speed error.
    if v <= 3:
        stdio.writeln("Value of v must be > 3 mph")
    else:
        # Write the wind chill w as standard output.
        stdio.writeln(w)
