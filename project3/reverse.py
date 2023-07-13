import stdio

# Accept all the strings from standard input and store them in a list a.
a = stdio.readAllStrings()

# Reverse a.
for i in range(len(a) // 2):
    # Iterate over half of the list a...

    # Exchange element at i in a with the element at len(a) - i - 1.
    a[i], a[len(a) - i - 1] = a[len(a) - i - 1], a[i]

# Write a to standard output.
for i in range(len(a)):
    if i < len(a):
        # If i is not the last column, write a[i] with a space after.
        stdio.write(a[i])
        stdio.write(" ")
    else:
        # Otherwise, write the element with a newline after.
        stdio.writeln(a[i])
