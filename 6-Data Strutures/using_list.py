# Filename: using_list.py
# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']
print('I have', len(shoplist), 'items to purchase.')
print('These items are:', end=' ') # print('', end = ' ')
for item in shoplist:
    print(item, end=' ')
print('\nI also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now', shoplist)
print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is', shoplist)
print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist)

# $ python using_list.py
#I have 4 items to purchase.
#These items are: apple mango carrot banana
#I also have to buy rice.
#My shopping list is now ['apple', 'mango', 'carrot', 'banana', 'rice']
#I will sort my list now
#Sorted shopping list is ['apple', 'banana', 'carrot', 'mango', 'rice']
#The first item I will buy is apple
#I bought the apple
#My shopping list is now ['banana', 'carrot', 'mango', 'rice']

