#

# Two ways in data list manager
list_new_data = ['a', 'b', 'c', 'd']

for i in list_new_data:
    if i == 'b':
        list_new_data.remove('b')
    else:
        continue
    
print(list_new_data)

new_list = []
for i in list_new_data:
    if i == 'b':
        continue
    else:
        new_list.append(i)
        
print(new_list)

# 