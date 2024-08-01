#

# Two ways in data list manager
list_new_data = ['a', 'b', 'c', 'd']

for i in list_new_data:
    if i == 'b':
        list_new_data.remove('b')
    else:
        continue
    
print(list_new_data)

list_new_data = ['a', 'b', 'c', 'd']
new_list = []
for i in list_new_data:
    if i == 'b':
        continue
    else:
        new_list.append(i)
        
print(new_list)

# Dicts

new_dict = {'a':1, 'b':2}

new_ = iter(new_dict)
#print(next(new_))

print(type(new_dict))
for i, x in new_dict.items():
    print('from new_dict: ', i)
    print('from new_dict value: ', x)

print(type(new_))
for u in new_:
    print('from new_: ', u)
    #>>b
    
    #print(next(u))
    #>>error
