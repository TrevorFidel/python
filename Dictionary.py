my_dictionary = {
    "Name": "Trevor",
    "Gender": "Male",
    "Status":"single"
}
print(my_dictionary)
my_dictionary = dict(
    Name="Trevor",
    Gender="Male",
    Status="single"
)
print(my_dictionary['Gender'])
print(my_dictionary.get('Status')) # prints specific  word in the dictionary.
print(my_dictionary['Name']) # prints specific  word in the dictionary.
my_dictionary['Status'] = "Complicated" # Edits the dictionary.
print(my_dictionary)
my_dictionary['BirthDate'] = "2003" # Adds a key value to the dictionary.
print(my_dictionary)
my_dictionary['Residence'] = "Syokimau" # Adding of an element to a dictionary.
print(my_dictionary)
my_dictionary2 = my_dictionary .copy()  # This copies items from the previous dictionary to the current one.
print(my_dictionary2)
print(len(my_dictionary)) # The inbuilt function len shows the length of a dictionary.
my_dictionary.pop('Status') # Removes a dictionary element.
print(my_dictionary)
del my_dictionary2['Status'] # Does the same function to the pop # means delete
print(my_dictionary2)
my_dictionary.clear() # Removes every element in the dictionary./ clears data only but not the entire dictionary.
print(my_dictionary)
del my_dictionary # Deletes the entire dictionary not just the elements. Doesnt exist in the memory.
# print(my_dictionary)
print(my_dictionary2)
if 'Name' in my_dictionary2: # Checks out a specific element in the dictionary.
    print('Name is in dictionary')
else:
    print('Name is not in dictionary')
for value in my_dictionary2:
    print(my_dictionary2[value]) # Prints dictionary values.
for key in my_dictionary2:
    print(key) # Prints the key elements in the dictionary.
for key, value in my_dictionary2.items():
    print(key, value)

    my_dict = {
        'Milk': 60,
        'Bread': 65,
        'Cooking oil': 350,
        'Sugar': 240,
        'Salt': 40
    }
    print(my_dict)
    if 'Sugar' in my_dict:
        print('Sugar available')
    else:
        print('No sugar available')
    my_dict['Body oil'] = 450
    print(my_dict)
    for key, value in my_dict.items():
        print(key, value)
