cnt = 0

with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.readlines() # 파일 전체의 라인 수 
    for i in text:
        cnt += 1 
    print(cnt)

with open('01.txt', 'w', encoding='utf-8') as f:
    f.write(str(cnt))