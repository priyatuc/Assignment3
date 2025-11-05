size = 5
hash_table = []

for i in range (0,size):
  hash_table.append([])

#returns the index
def hash_function(key, size):
  return (key % size)  

#inserts key-value pair into hash table
def insert(key, value):
  index = hash_function(key, size)
  hash_table[index].append((key, value))

#searches for value by key
def search(key):
  index = hash_function(key, size)
  data = hash_table[index]
  for k, v in data:
    if k == key:
      return v
  return ("Key did not match, No value returned.")

  #deletes key-value pair from hash table
def delete(key):
  index = hash_function(key, size)
  data = hash_table[index]
  for item in data:
    if item[0] == key:
      data.remove(item)
      return ("Data removed.")
  return ("Could not find the data, no data was removed")

# inserting some key-value pairs
insert(1, "apple")
insert(2, "banana")
insert(3, "grapes")
insert(4, "orange")
insert(5, "mango")
insert(6, "berries")

print("The hash table is:")
for i, chain in enumerate(hash_table):
    print(f"{i}: {chain}")

print ("Deleting Key 1:", delete(1))

print("The hash table after deleting Key 1:")
for i, chain in enumerate(hash_table):
    print(f"{i}: {chain}")







