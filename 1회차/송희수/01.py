with open('fruits.txt', 'r', encoding='utf-8') as f:
        text = f.readlines()
        cnt = 0
        for i in text:
            cnt += 1
            print(cnt)
with open('01.txt', 'w' , encoding='utf-8') as f:
    f.write('394')