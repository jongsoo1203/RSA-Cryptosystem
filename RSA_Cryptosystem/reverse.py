import stdio


# Entry point (DO NOT EDIT).
def main():
    a = stdio.readAllStrings()
    _reverse(a)
    for v in a[:-1]:
        stdio.writef('%s ', v)
    stdio.writeln(a[-1])


# Reverses a in place, ie, without creating a new list.
def _reverse(a):
    for i in range(len(a) // 2):
        # Iterate over half of the list a...

        # Exchange element at i in a with the element at len(a) - i - 1.
        a[i], a[len(a) - i - 1] = a[len(a) - i - 1], a[i]


if __name__ == '__main__':
    main()
