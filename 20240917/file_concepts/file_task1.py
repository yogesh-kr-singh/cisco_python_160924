# lst = list(map(str,input().split()))
# tup = tuple(lst)

# with open("fruits_names.txt", "w") as file:
#     file.write("List: " + str(lst) + "\n")
#     file.write("Tuple: " + str(tup) + "\n")
    
    
# with open('fruits_names.txt', 'r') as file:
#     line1 = file.readline()
#     line2 = file.readline()
#     print(line1)
#     print(line2)
    
    
    
    
# ---------------------------------------------------------------
import json
names_list = input('Enter student names (seperated by space): ').split()
names_set = set(names_list)
names_frozen = frozenset(names_set)
names_dict = {name:len(name) for name in names_frozen} #dict comprehension technique

print(f'Original List : {names_list}')
print(f'Set (no duplicates): {names_set}')
print(f'Frozen set: {names_frozen}')
print(f'Dictionary of name lengths: {names_dict}')


with open('task2_data.json','w') as file:
    json.dump(names_dict,file)

print("Dictionary written to JSON file")

with open('task2_data.json','r') as file:
    names_dict1 = json.load(file)
