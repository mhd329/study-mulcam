from anyio import open_file


with open('1.txt', 'w', encoding='UTF-8') as f:
    with open('data/fruits.txt','r', encoding='UTF=8') as f1:
        text = f1.readlines()
        cnt = 0
        for i in text:
            cnt += 1
    f.write(str(cnt))

