with open('data/fruits.txt', 'r', encoding = 'UTF-8') as f:
    lines = f.read()
    names = lines.split()
    names_ok = set(names) 
    cnt = 0

    for i in names_ok:
        if i[-5:] == 'berry':
            print(i)
            cnt += 1

    print(cnt)

            
