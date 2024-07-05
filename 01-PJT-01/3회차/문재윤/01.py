with open('data/fruits.txt', 'r', encoding="UTF8") as data:
    contents = data.read()
    contents = (contents.split('\n'))

    s = 0
    for i in contents:
        s +=1
    print(s)

    with open('01.txt', 'w', encoding='utf-8') as ff:
        ff.write(f'{s}')


