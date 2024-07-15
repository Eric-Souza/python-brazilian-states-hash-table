class Node:
    def __init__(self, abbreviation, stateName):
        self.abbreviation = abbreviation
        self.stateName = stateName
        self.next = None

class HashTable:
    def __init__(self):
        self.table = [None] * 10  # 10 positions, initially None

    def hash_function(self, abbreviation):
        if abbreviation == "DF":
            return 7
        else:
            return (ord(abbreviation[0]) + ord(abbreviation[1])) % 10

    def insert(self, abbreviation, stateName):
        position = self.hash_function(abbreviation)
        new_node = Node(abbreviation, stateName)
        if self.table[position] is None:
            self.table[position] = new_node
        else:
            current = self.table[position]
            new_node.next = current
            self.table[position] = new_node

    def print_table(self):
        for i in range(10):
            print(f"Position {i}:", end=" ")
            current = self.table[i]
            while current is not None:
                print(f"{current.abbreviation} ({current.stateName})", end=" -> ")
                current = current.next
            print("None")

# States and Federal District
states = [
    ("AC", "Acre"), ("AL", "Alagoas"), ("AP", "Amapá"), ("AM", "Amazonas"), ("BA", "Bahia"),
    ("CE", "Ceará"), ("DF", "Federal District"), ("ES", "Espírito Santo"), ("GO", "Goiás"),
    ("MA", "Maranhão"), ("MT", "Mato Grosso"), ("MS", "Mato Grosso do Sul"), ("MG", "Minas Gerais"),
    ("PA", "Pará"), ("PB", "Paraíba"), ("PR", "Paraná"), ("PE", "Pernambuco"), ("PI", "Piauí"),
    ("RJ", "Rio de Janeiro"), ("RN", "Rio Grande do Norte"), ("RS", "Rio Grande do Sul"),
    ("RO", "Rondônia"), ("RR", "Roraima"), ("SC", "Santa Catarina"), ("SP", "São Paulo"),
    ("SE", "Sergipe"), ("TO", "Tocantins")
]

# Fictitious state
fictitious_state = ("BK", "Bruno Kostiuk")

# Instantiate the hash table
hash_table = HashTable()

# Console output requirement 1 of 3: Print hash table before inserting any information
print("Hash table before inserting any information:")
hash_table.print_table()

# Code requirement 6 of 7: Insert 26 states and the Federal District
for abbreviation, name in states:
    hash_table.insert(abbreviation, name)

# Console output requirement 2 of 3: Print hash table after inserting 26 states and the Federal District
print("\nHash table after inserting 26 states and the Federal District:")
hash_table.print_table()

# Code requirement 7 of 7: Insert fictitious state
hash_table.insert(fictitious_state[0], fictitious_state[1])

# Console output requirement 3 of 3: Print hash table after inserting 26 states, the Federal District, and the fictitious state
print("\nHash table after inserting 26 states, the Federal District, and the fictitious state:")
hash_table.print_table()
