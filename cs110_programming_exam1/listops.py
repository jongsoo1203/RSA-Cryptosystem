# Returns True if any value in the list a is True, and False otherwise.
def any(a):
    for i in a:
        if i is True:
            return True
    return False

# Returns True if all values in the list a are True, and False otherwise.
def all(a):
    for i in a:
        return i == True

# Returns True if exactly k values in the list a are True, and False otherwise.
def exactly(a, k):

    count = 0

    for i in a:
        if i is True:
            count += 1

    return count == k

# Returns the number of True values in the list a.
def count(a):
    count = 0

    for i in a:
        if i == True:
            count += 1

    return count

# Unit tests the library.
def _main():
    import stdio

    a = [False, True, False, False, True, True, True]
    stdio.writeln('a             = ' + str(a))
    stdio.writeln('any(a)        = ' + str(any(a)))
    stdio.writeln('all(a)        = ' + str(all(a)))
    stdio.writeln('exactly(a, 3) = ' + str(exactly(a, 3)))
    stdio.writeln('count(a)      = ' + str(count(a)))


if __name__ == '__main__':
    _main()
