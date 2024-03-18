my_set = {1, 2, 3, 4, 5}
print(my_set) # A set does not use indexes hence one must narrow down by involving a variable. /// Its not ordered.
var1 = 2
if var1 in my_set:
    print(var1)
var2 = 5
if var2 in my_set:
    print(var2)
my_set.add(9) # adds a value in the set. Only allows one value
print(my_set)
my_set.update([7, 10, 12, 14]) # Adds more than one value.
print(my_set)
my_set2 = my_set.copy() # For coping values in different sets.
print(my_set2)
print(my_set)
print(max(my_set))
print(min(my_set))
print(sum(my_set))
print(sum(my_set)/len(my_set))
my_set.discard(7)
my_set.clear()
del my_set
if 32 in my_set2:
    print('32 in my_set2')
else:
    print('32 not in my_set2')