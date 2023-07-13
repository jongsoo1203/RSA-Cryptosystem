import math
import stdio
import sys

# Accept Latitude (float) and Longitude (float) as command-line arguments.
Latitude = float(sys.argv[1])
Longitude = float(sys.argv[2])

# find the projection by using the equation
x = Longitude
y = math.log((1 + math.sin(math.radians(Latitude))) / (1 - math.sin(math.radians(Latitude)))) / 2

# Write the longitude and the projection to standard output.
stdio.writeln(str(x) + " " + str(y))
