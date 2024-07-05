with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    #print(text, type(text))
    names = text.split('\n')
    #print(names, type(names))
    count = 0
    for name in names:
        count += 1

with open('01.txt', 'w', encoding='utf-8') as g:
    g.write(f'{count}')
