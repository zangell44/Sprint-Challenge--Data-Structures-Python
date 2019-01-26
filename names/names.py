import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

names_2 = set(names_2)

duplicates = []
for name in names_1:
    if name in names_2:
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime 1 : {end_time - start_time} seconds")

### Constrained Memory - Only Stored in Arrays ###
# cant use a set because hashtables waste lots of memory

def binary_search(val, array, low, high):
    
    while low < high:
        mid = (low + high) // 2
        
        if val == array[mid]:
            return True
        elif val > array[mid]:
            low = mid + 1
        else:
            high = mid
    return False

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

names_2.sort()
names_2_len = len(names_2)

duplicates = []
for name in names_1:
    if binary_search(name, names_2, 0, names_2_len-1):
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime 1 : {end_time - start_time} seconds")
