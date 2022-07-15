with open('data/fruits.txt', 'r', encoding = 'utf-8') as f: # f란 이름으로 fruits.txt를 읽기 전용으로 열 건데
    text = f.read() # 이 문자열(==text) 안의
    noblank = text.replace(' ', '') # 공백을 지우고(==noblank)
    fruits = noblank.split() # 이걸 리스트로 만들어서(==fruits)
    print(len(fruits)) # 이 리스트의 길이를 출력함