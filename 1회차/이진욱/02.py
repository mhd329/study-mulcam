with open('data/fruits.txt', 'r',encoding='utf-8') as f:
    
    f_set=set()
    while True:
        text02 = f.readline()
        if text02.endswith('berry\n'):
            f_set.add(text02)
            
        if text02 == '':
            break

    d= open('02.txt','w',encoding='utf-8')
    d.write(f'{len(f_set)}\n')
    for i in range(len(f_set)):
        d.write(list(f_set)[i])
