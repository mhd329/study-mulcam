
with open('2.txt', 'w', encoding='UTF-8') as f:
    with open('data/fruits.txt','r', encoding='UTF=8') as f1:
        text = f1.readlines()
        li = set()
        for i in text:
            if 'berry' in i[1:]:
                li.add(i)
        f.write(f'{len(li)}\n')
        for i in li:
            f.write(i)

