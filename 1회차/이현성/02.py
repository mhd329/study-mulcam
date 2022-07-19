berry = set()
with open('data/fruits.txt', 'r', encoding='utf-8') as f :
    text = f.read()
    fruit = text.split('\n')
    for name in fruit : 
        if name.endswith('berry') == True :
            berry.add(name)

with open('02.txt', 'w', encoding='utf-8') as f :
    f.write(f'{len(berry)}\n')
    for i in range(len(berry)) :
        f.write(f'{berry.pop()}\n') 