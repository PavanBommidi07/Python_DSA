hash_table = [[] for _ in range(10)]

def hashing(keyvalue):
    return keyvalue % len(hash_table)

def insert(hash_table,keyvalue,value):
    hash_key = hashing(keyvalue)
    hash_table[hash_key].append(value)

def display(keyvalue):
    h = hashing(keyvalue)
    return hash_table[h]

insert(hash_table,10,"suryapet")
insert(hash_table,23,"khammam")
insert(hash_table,20,"warangal")
insert(hash_table,45,"kodad")
var = display(20)
print(var)
var = display(23)
print(var)