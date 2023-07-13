import stdio
import sys


# Entry point [DO NOT EDIT].
def main():
    s = sys.argv[1]
    stdio.writeln(_reverse(s))


# Returns the reverse of the string s.
def _reverse(s):
    # Base case: if s is the empty string, return an empty string.
    if len(s) == 0:
        return ""

    # Recursive step: return last character in s + _reverse(s excluding last character).
    return s[len(s) - 1] + _reverse(s[0:len(s) - 1])


if __name__ == '__main__':
    main()
