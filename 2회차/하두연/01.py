with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    count = 0
    text = f.read()
    lines = text.split('\n')

    for line in  lines:
        count += 1

    with open('01.txt', 'w', encoding='utf-8') as a:
        a.write(f'{count}')
    




