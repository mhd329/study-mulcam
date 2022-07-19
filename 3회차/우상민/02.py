


count = 0

with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
       text = f. read()
       fruit1 = text.split('\n')
       fruit2 = set(fruit1)
       for i in fruit2:
        if i.endswith('berry'):
            count += 1 
            print(i)
       print(count)

