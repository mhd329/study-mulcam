with open('2.txt', 'w', encoding='UTF-8') as f:
    with open('data/fruits.txt','r', encoding='UTF=8') as f1:
        # text = f1.readline() # 1줄
        # text = f1.readlines() # 리스트 형 반환, 개행문자 (\n) 포함
        text = f1.read()
        print(text)