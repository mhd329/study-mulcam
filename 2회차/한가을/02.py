with open('data/fruits.txt', 'r') as f:
    lines = f.readlines()

    # for line in lines:
    #     line = line.strip()
    #     print(line)

    result = []
    count = 0

    for i in lines:
        str = i[:-1]
        if str[-5:] == 'berry':
            result.append(i)

    n = len(set(result))


with open('02.txt', 'w', encoding = 'utf-8') as f:
    f.write(f'{n}\n')
    for i in set(result):
        f.write(i)