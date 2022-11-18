input_list = [100, 75, 100, 20, 75, 12, 75, 25, 75, 100, 'a', 'b', 'a', 'b', '?', '/', '?', 'a'] 

output_list = []

for item in input_list: 
    if item not in output_list: 
        output_list.append(item) 

print('Unique elements of the list:')
for item in output_list: 
    print(item)