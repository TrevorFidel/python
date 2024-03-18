my_list = [113, 245, 368, 466, 587, 435,]
print(my_list) # list are ordered from index 0.
print(my_list[4])
print(my_list[2:4]) # This prints out a given range.
my_list[1] = 345
print(my_list) # Corrects/updates out a given figure in  the list.
my_list[4] = 700
print(my_list)
print(len(my_list)) # Shows the number of items in the list.
my_list.append(361)  # Adds a value that is to be added in the list.
print(my_list)
my_list.insert(1,297) # Adds a value at a specific point.
print(my_list)
my_list.extend([123, 434, 345, 297])
my_list.remove(368) # Removes a value in the list.
print (my_list)
del my_list[3] # Gets rid of a specific value in the given index.
my_list.clear() # Erraces the  list values.
# del my_list() # deletes the entire list.

my_list2 = [134, 345, 567, 765, 657, 856, 300]
print(max(my_list2)) # shows the max figure.
print(min(my_list2)) # Shows the min figure.
print(sum(my_list2)) # Gets the total of the list.
print(sum(my_list2)/len(my_list2))
if 765 in my_list2:
    print('Present')
else:
    print('Not present')
# ASSESMENT
my_list3 = ['Trevor', 'John', 'Smith', 'Cecilia', 'Joel']
print(my_list3)
if 'Cecilia' in my_list3:
    print('Cecilia present')
else:
    print('Cecilia absent')