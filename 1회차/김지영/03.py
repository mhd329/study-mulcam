with open('data/fruits.txt', 'r', encoding='utf-8') as f, open('03.txt', 'w', encoding='utf-8') as text03 :
    fruit = f.read()
    fruit_split = fruit.split('\n')
    # print(fruit_split, type(fruit_split))
    result = {}
    for line in fruit_split:
        # print(line)
        result[line] = result.get(line,0) +1
    # print(result, type(result))

    for key in result:
        # print(f'{key} : {result[key]}\n')
        text03.write(f'{key} : {result[key]}\n')
        
