with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    fruits = text.split("\n")
    result = []
    cnt = 0

    for i in fruits:
        if i not in result:
            result.append(i)

with open('02.txt', 'w', encoding='utf-8') as f:
    for fruit in result:
        if fruit[-5:] == 'berry':
            cnt += 1
    cnt = str(cnt)
    print(cnt)
    f.write(cnt)
    f.write("\n")

    for fruit in result:
        if fruit[-5:] == 'berry':
            print(fruit)
            f.write(fruit+"\n")