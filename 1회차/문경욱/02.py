cnt = 0
friut_list= []
with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    for name in f:
        if name.endswith('berry\n'):
            friut_list.append(name)
friut_list = set(friut_list)
num_fruit = len(friut_list)

# print(num_fruit)
# for i in friut_list:
#     print(i.rstrip('\n'))

with open('02.txt', 'w', encoding='utf-8') as f:
    f.write(f'{num_fruit}\n')
    for i in friut_list:
        f.write(i)