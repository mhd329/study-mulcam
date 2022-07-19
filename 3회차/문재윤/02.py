


with open('data/fruits.txt', 'r', encoding="UTF8") as data:
    contents = data.read()
#print(type(contents))
    contents = (contents.split('\n'))
    contents = list(set(contents))
    with open('02.txt', 'w', encoding='utf-8') as ff:
        s = 0
        for i in contents:
            if 'berry' in i:
                if i[-5:] == 'berry':
                   s +=1
        ff.write(f'{s}\n') 

        for i in contents:
            if 'berry' in i:
                if i[-5:] == 'berry':
                    ff.write(f'{i}\n')







