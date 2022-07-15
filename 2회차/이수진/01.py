with open("2회차/이수진/data/fruits.txt", 'r',encoding='utf=8') as f:
    with open("2회차/이수진/data/01.txt", 'w',encoding='utf=8') as f2:
        f=list(f)
        f2.write(str(len(f)))