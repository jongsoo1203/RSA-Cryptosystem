import stdio
import sys

# Accept month (int), day (int) year (int) as command-line arguments.
m = int(sys.argv[1])
d = int(sys.argv[2])
y = int(sys.argv[3])

# calculate which day of weekend is
y0 = y - (14 - m) // 12
x0 = y0 + y0//4 - y0 // 100 + y0 // 400
m0 = m + 12 * ((14 - m) // 12) - 2
dow = (d + x0 + 31 * m0 // 12) % 7

# Write the day of weekend to standard output.
stdio.writeln(dow)
