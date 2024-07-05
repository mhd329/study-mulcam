with open('data/fruits.txt','r',encoding='utf-8')as f:
    for line in f:
        if 'berry' in line:
            print(line, end='')
