with open('./data/fruits.txt', 'r', encoding='utf-8') as file:
    
    lines = file.readlines()
    fruits = dict()
    
    for line in lines:
        if line in fruits :
            fruits[line] += 1
        else:
            fruits[line] = 1

with open('03.txt', 'w', encoding='utf-8') as file:
    for key, value in fruits.items():
        file.write("{} {}\n".format(key.rstrip('\n'), fruits[key]))
    
    