from instream import InStream
from symboltable import SymbolTable
import stdio
import sys


# Entry point.
def main():
    # Accept filename (str) as command-line argument.


    # Set inStream to an input stream built from filename.
    ...

    # Set words to the list of strings read from inStream.
    ...

    # Set occurrences to a new symbol table object.
    ...

    for i, word in enumerate(...):
        # For each word (having index i) in words...

        # If word does not exist in occurrences, insert it with an empty list as the value.
        ...

        # Append i to the list corresponding to word in occurrences.
        ...

    while ...:
        # As long as standard input is not empty...

        # Set word to a string read from standard input.
        ...

        # If word exists in occurrences, write the word and the corresponding list to standard
        # output, separated by the string '->'. Otherwise, write the message 'Word not found'.
        if ...:
            ...
        else:
            ...


if __name__ == '__main__':
    main()
