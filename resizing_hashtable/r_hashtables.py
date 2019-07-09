

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for item in string:
        hash = ((hash << 5) + hash) + ord(item)
    return hash % max


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    hashed_key = hash(key, hash_table.capacity)

    item_to_store = LinkedPair(key, value)

    item_at_index = hash_table.storage[hashed_key]

    # handle if value at index is None
    if hash_table.storage[hashed_key] is None:
        hash_table.storage[hashed_key] = item_to_store

    # handle if there is a collision
    else:
        while item_at_index:
            if item_at_index.key == key:
                item_at_index.value = value
                return
            elif item_at_index.next == None:
                item_at_index.next = item_to_store
                return
            else:
                item_at_index = item_at_index.next


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    hashed_key = hash(key, hash_table.capacity)
    item_at_index = hash_table.storage[hashed_key]

    if hash_table.storage[hashed_key] == None:
        print('Warning: there is nothing at index' +
              str(hashed_key) + ' to remove')

    else:
        while item_at_index:
            if item_at_index.key == key:
                # if next is None set the index to None
                if item_at_index.next == None:
                    hash_table.storage[hashed_key] = None
                # else set the cur
                else:
                    hash_table.storage[hashed_key] = item_at_index.next
                return

            # continue traversing
            else:
                item_at_index = item_at_index.next
    print('item does not exist in storage')


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    hashed_key = hash(key, hash_table.capacity)

    item_at_index = hash_table.storage[hashed_key]

    while item_at_index:
        if item_at_index.key == key:
            return item_at_index.value
        else:
            item_at_index = item_at_index.next

    else:
        return None


def hash_table_resize(hash_table):

    new_hash_table = HashTable(hash_table.capacity * 2)

    for obj in hash_table.storage:
        hash_table_insert(new_hash_table, obj.key, obj.value)

    return new_hash_table


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
