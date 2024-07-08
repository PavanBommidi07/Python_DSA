# def hash_function(key):
#     hash = 0
#     for char in key:
#         hash += ord(char)
#     return hash % 10

# value = hash_function("pavan")
# print(value)

hash_table = [[] for _ in range(10)]
def hash_function(key):
    hash = 0
    for char in key:
        hash += ord(char)
    return hash % 10
def insert(key, data):
    h = hash_function(key)
    hash_table[h] = data
def get_data(key):
    h = hash_function(key)
    return hash_table[h]

insert_data = insert(123,'suniya')
insert_data = insert(456, 'pavan')
insert_data = insert(789,'dell')


