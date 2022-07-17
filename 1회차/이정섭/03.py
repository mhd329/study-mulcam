f_dict = {}

with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    list = f.read()
    fruits = list.split('\n')
   
    for fruit in fruits:
        if fruit in f_dict:
            f_dict[fruit] += 1
        else:
            f_dict[fruit] = 1

with open('03.txt', 'w', encoding='utf-8') as f:
    for fruit in f_dict:
        f.write(f"{fruit}")
        f.write(f"{f_dict[fruit]}\n")
    