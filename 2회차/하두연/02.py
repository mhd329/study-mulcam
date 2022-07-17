with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    names = text.split('\n')
    count = 0
    a = []

   
    
    for i in names:
        if i.endswith('berry'):
            if not i in a: #. not ~ in 텍스트(리스트) 내에 값이 없는지 확인
                count += 1
                a.append(i)

    with open('02.txt', 'w', encoding='utf-8')as c:
        c.write(f'{count}\n')

        for i in a:
            c.write(f'{i}\n')
            


    



       

