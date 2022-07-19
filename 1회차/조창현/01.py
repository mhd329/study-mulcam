with open('data/fruits.txt', 'r', encoding = 'utf-8')as f:
    fruits = f.readlines()
    # print(text, type(text))
    cnt = 0
    for fruit in fruits:
        if fruit != 0:
            cnt += 1
    print(cnt)