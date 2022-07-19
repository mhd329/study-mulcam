fruit_list = []
fruit_dict = {}

with open('data\\fruits.txt', 'r') as f:
    lines = f.readlines()

fruit_list = list(map(lambda s: s.strip(), lines))
    
for fruit_list_element in fruit_list:
    fruit_dict[fruit_list_element] = fruit_dict.get(fruit_list_element, 0) + 1

with open('03.txt', 'w') as f1:
    for k, v in fruit_dict.items():
        f1.writelines([k, " ", str(v), '\n'])