import stdio
import sys


# Entry point (DO NOT EDIT).
def main():
    s = sys.argv[1]
    stdio.writeln(_isPalindrome(s))


# Returns True if s is a palindrome and False otherwise.
def _isPalindrome(s):
    for i in range(len(s) // 2):
        # Iterate over half of the string s...

        # If the character at i is different from the character at len(s) - i - 1, s is not a
        # palindrome, so return False.
        if s[i] != s[len(s) - i - 1]:
            return False

    # s is a palindrome, so return True.
    return True


if __name__ == '__main__':
    main()
