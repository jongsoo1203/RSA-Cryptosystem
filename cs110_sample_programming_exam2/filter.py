from circle import Circle
import stdio
import sys


# Entry point.
def main():
    h = float(sys.argv[1])
    k = float(sys.argv[2])
    r = float(sys.argv[3])

    c = Circle(h, k, r)

    total = 0
    inside = 0

    while not stdio.isEmpty():
        x = stdio.readFloat()
        y = stdio.readFloat()
        total += 1

        if c.contains(x, y):
            inside += 1

    stdio.writeln(inside / total)


if __name__ == '__main__':
    main()
