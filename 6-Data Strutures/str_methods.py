
# Filename: str_methods.py
name = 'Swaroop' # This is a string object
if name.startswith('Swa'):
    print('Yes, the string starts with "Swa"')
if 'a' in name:
    print('Yes, it contains the string "a"')
if name.find('war') != -1:
    print('Yes, it contains the string "war"')
delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))

# Output:
#   $ python str_methods.py
#   Yes, the string starts with "Swa"
#   Yes, it contains the string "a"
#   Yes, it contains the string "war"
#   Brazil_*_Russia_*_India_*_China
