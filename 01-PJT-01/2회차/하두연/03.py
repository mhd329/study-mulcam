with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    names = text.split('\n')
    fruits = {}

    for name in names:
        if not name in fruits:
            fruits[name] = 1
        else:
            fruits[name] +=1

with open('03.txt', 'w', encoding='utf-8') as f:
    for a, b in fruits.items():
        # dic.item() ----> dic안의 모든 item 출력
            f.write(f'{a} {b}\n')

