with open('./data/fruits.txt','r',encoding='utf-8')as f, open('03.txt','w',encoding='utf-8')as file :
    fruit = f.read()
    fruit = fruit.split('\n')
    fruits = {}
    a = []
    for i in fruit:
        fruits[i] = 0
        for j in fruit:
            if i == j:
                fruits[i] += 1
    for key, value in fruits.items():
        print(key, value)
        a = key
        print(a)
    for key in fruits:
        # print(f'{key} : {result[key]}\n')
        file.write(f'{key} : {fruits[key]}\n')