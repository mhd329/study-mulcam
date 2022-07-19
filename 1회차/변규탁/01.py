with open('./data/fruits.txt', 'r', encoding='utf-8') as file:
    line = file.readlines()
    count = 0
    for i in line:
        count += 1
    print(count)