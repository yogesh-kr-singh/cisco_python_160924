# using 'with' clause ----------------------------------------
'''
with open('names.txt', 'r') as names_db :
    all_names = names_db.read()
    print(all_names)
    print('--------------------')
'''

# without using 'with' clause --------------------------------
'''
names_db = open ('names.txt', 'r')
all_names = names_db.read()
print(all_names)
'''




