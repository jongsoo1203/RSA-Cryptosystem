import stdio
import sys


# Entry point [DO NOT EDIT].
def main():
    pwd = sys.argv[1]
    stdio.writeln(_isValid(pwd))


# Returns True if pwd is a valid password, and False otherwise.
def _isValid(pwd):
    check1 = False  # length flag
    check2 = False  # digit flag
    check3 = False  # upper case flag
    check4 = False  # lower case flag
    check5 = False  # alphanumeric flag

    # If c is long enough, set corresponding flag to True.
    if len(pwd) >= 8:
        check1 = True

    for c in pwd:
        # For each character c in pwd...

        if c.isdigit():
            # If c is a digit, set corresponding flag to True.
            check2 = True
        elif c.isupper():
            # If c is in upper case, set corresponding flag to True.
            check3 = True
        elif c.islower():
            # If c is in lower case, set corresponding flag to True.
            check4 = True
        elif not c.isalnum():
            # If c is not alphanumeric, set corresponding flag to True.
            check5 = True

    # Return True if all flags are True, and False otherwise.
    if check1 and check2 and check3 and check4 and check5:
        return True
    return False


if __name__ == '__main__':
    main()
