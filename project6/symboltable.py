# A data type to represent a symbol table of key-value pairs.

import stdio


class SymbolTable:
    # Constructs an empty symbol table.
    def __init__(self):
        self._st = dict()  # dictionary of key-value pairs

    # Returns True if this symbol table is empty, and False otherwise.
    def isEmpty(self):
        return len(self._st) == 0

    # Returns the number of key-value pairs in this symbol table.
    def __len__(self):
        return len(self._st)

    # Returns True if this symbol table contains key, and False otherwise.
    def __contains__(self, key):
        return key in self._st

    # Returns the value associated with key in this symbol table.
    def __getitem__(self, key):
        return self._st[key]

    # Inserts a key-value pair into this symbol table.
    def __setitem__(self, key, val):
        self._st[key] = val

    # Returns the keys in this symbol table, as an iterable object.
    def keys(self):
        return iter(self._st.keys())

    # Returns the values in this symbol table, as an iterable object.
    def values(self):
        return iter(self._st.values())


# Unit tests the data type.
def _main():
    st = SymbolTable()
    st['Gautama'] = 'Siddhartha'
    st['Darwin'] = 'Charles'
    st['Einstein'] = 'Albert'
    stdio.writeln(st['Gautama'])
    stdio.writeln(st['Darwin'])
    stdio.writeln(st['Einstein'])
    if 'Einstein' in st:
        stdio.writeln('Einstein found')
    else:
        stdio.writeln('Einstein not found')
    if 'Newton' in st:
        stdio.writeln('Newton found')
    else:
        stdio.writeln('Newton not found')
    for key in st.keys():
        stdio.writeln(key + ': ' + st[key])
    for value in st.values():
        stdio.writeln(value)


if __name__ == '__main__':
    _main()
