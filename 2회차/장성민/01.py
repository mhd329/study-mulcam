with open('data/fruits.txt', encoding = 'UTF8') as f:
    lines = f.readlines()
    count = 0
    for i in lines:
        count += 1

    print(count)
        