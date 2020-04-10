class HashTable:
    def __init__(self):
        self.table = [None] * 10

    def store(self, string):
        hv = self.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] is not None:
                self.table[hv].append(string)
            else:
                self.table[hv] = [string]
        return self.table

    def lookup(self, string):
        hv = self.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] is not None:
                if string in self.table[hv]:
                    return hv
        return -1

    def calculate_hash_value(self, string):
        value = ord(string[0]) * 100 + ord(string[1])
        value = value % len(self.table)
        return value


hash_table = HashTable()
hash_table.store('paul')
hash_table.store('akb')
hash_table.store('bhd')
hash_table.store('cecil')
print(hash_table.table)
print(hash_table.lookup('akb'
                        ''))
# print(hash_table.store('paul', 18))
# print(hash_table.store('aub', 18))
