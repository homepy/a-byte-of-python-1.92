
# Filename: using_tuple.py
zoo = ('python', 'elephant', 'penguin') # remember the parentheses are optional
print('Number of animals in the zoo is', len(zoo))
new_zoo = ('monkey', 'camel', zoo)
print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is', len(new_zoo)-1+len(new_zoo[2]))

# Number of animals in the zoo is 3
# Number of cages in the new zoo is 3
# All animals in new zoo are ('monkey', 'camel', ('python', 'elephant', 'penguin'))
# Animals brought from old zoo are ('python', 'elephant', 'penguin')
# Last animal brought from old zoo is penguin
# Number of animals in the new zoo is 5
