with open('data/fruits.txt' , 'r' , encoding = 'utf-8') as f:
    lines = f.readlines()
    
with open('02.txt' , 'w' , encoding = 'utf-8') as f:
    count = 0
    text = []
    for a in lines:
        new = a.strip('\n')
        if new.endswith('berry'):
            text.append(new)

    new_text = set(text)
    
    for b in set(text):
        count += 1
        f.write(b + '\n')
    f.write(str(count))

    
