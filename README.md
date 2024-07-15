# State Registration Hash Table

This program implements a hash table with separate chaining for storing state registration information. Each position in the hash table is a linked list, and the table has 10 positions.

## Features

- Each node in the linked list represents a state with its abbreviation and name.
- The hash function is based on the ASCII values of the abbreviation characters.
- The hash function has a special rule for the Federal District ("DF"), which always maps to position 7.

## Classes and Methods

### `Node` Class
Represents a node in the linked list with the following attributes:
- `abbreviation`: The state's abbreviation.
- `stateName`: The state's name.
- `next`: Pointer to the next node.

### `HashTable` Class
Represents the hash table and provides methods to manage it.

#### Methods

- `hash_function(abbreviation)`: Computes the hash value for a given state abbreviation.
- `insert(abbreviation, stateName)`: Inserts a new state node into the hash table.
- `print_table()`: Prints the entire hash table, showing the states in each position.
