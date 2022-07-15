with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    fruits = text.split('\n')
    d = {}
    for i in fruits:
        if not i in d:
            d[i] = 1
        else:
            d[i] += 1
   
with open('03.txt', 'w', encoding='utf-8') as f:
     for key, value in d.items():
        # print(key, value)
        result = ' '.join(map(str,(key, value)))
        # print(result)
        f.write(f'{result}\n')