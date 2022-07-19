with open('data/fruits.txt', 'r', encoding='utf-8') as f: # data 폴더에 있는 fruits.txt 파일 오픈 r = 읽기
    text = f.readlines() # 전체 내용을 한 줄마다 불러오기
    print(len(text)) # len 함수 이용 몇개의 readlines 있는지 확인