my_tuple = (111, 652, 873, 654, 565) # A tuple uses this brackets not square brackets like a list.
print(my_tuple)
print(my_tuple[2])
print(my_tuple[3:5])
print(len(my_tuple))
del my_tuple
my_tuple2 = (111, 652, 873, 654, 432, 789, 652)
print(my_tuple2.count(652))
print(max(my_tuple2))
print(min(my_tuple2))
print(sum(my_tuple2))
print(sum(my_tuple2)/len(my_tuple2))
print(my_tuple2.index(873))
if 652 in my_tuple2:
    print('652 is in my_tuple2')
else:
    print('652 is not in my_tuple2')
# DOES NOT ALLOW MODIFICATION LIKE IN THE LIST. Hence the difference.
# Best for static data that should not be changed.