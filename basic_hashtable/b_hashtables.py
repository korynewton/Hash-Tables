

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.storage = [None] * capacity
        self.capacity = capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for item in string:
        hash = ((hash << 5) + hash) + ord(item)
    return hash & 0xFFFFFFFF % max


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    hashed_key = hash(key, hash_table.capacity)
    if hash_table.storage[hashed_key]:
        print('warning: overwritting')
    hash_table.storage[hashed_key] = Pair(hashed_key, value)


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    hashed_key = hash(key, hash_table.capacity)
    if hash_table.storage[hashed_key] == None:
        print('Warning: No value at this key')
        return
    else:
        hash_table.storage[hashed_key] = None


# '''
# Fill this in.

# Should return None if the key is not found.
# '''

def hash_table_retrieve(hash_table, key):
    hashed_key = hash(key, hash_table.capacity)
    if not hash_table.storage[hashed_key]:
        return None
    else:
        return hash_table.storage[hashed_key].value


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()

# ht = BasicHashTable(100)
# print(ht.storage)
# print(hash('test', ht.capacity))
# print(hash('testfer', ht.capacity))
# print(hash('testfasf', ht.capacity))
# print(hash('testwfaa', ht.capacity))
# print(hash('tesfwt', ht.capacity))
# print(hash('tewfarst', ht.capacity))
# print(hash('tfweqest', ht.capacity))
# print(hash('tfweest', ht.capacity))
# print(hash('tfewest', ht.capacity))

# hash_table_remove(ht, 'testing')
# hash_table_insert(ht, 'testing', 'is good')
# print(ht.storage[hash('testing', ht.capacity)])
# hash_table_insert(ht, 'testing', 'is very good')
# print(ht.storage[hash('testing', ht.capacity)])

# print('after adding', hash_table_remove(ht, 'testing'))
# hash_table_remove(ht, 'testing')

# ht = BasicHashTable(8)

# hash_table_insert(ht, "key-0", "new-val-0")
# return_value = hash_table_retrieve(ht, "key-0")
# print('return value:', return_value)
