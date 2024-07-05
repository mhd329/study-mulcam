with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    fruits = f.readlines()
    cnt = 0
    names = ['berry']
    print(names)
    cnt = 0
    result = []
    for i in names:
        if 'berry' in i:
            cnt += 1
            result += [i]
    print(cnt, result)
    


