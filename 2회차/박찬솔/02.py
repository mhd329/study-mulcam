with open('data/fruits.txt','r',encoding='utf-8') as f:
    text = f.read()
    print(text, type(text))
with open('01.txt','w',encoding='utf-8') as f:
    names = text.split()
    cnt += 0
    for name in names:
        if name.startswith('berry'):
            cnt += 1
    print(cnt)