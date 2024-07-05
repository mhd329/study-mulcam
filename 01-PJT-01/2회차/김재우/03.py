with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.readlines() # readlines 이용 txt 불러오기
    result = {} # result 라는 키와 값을 가지는 딕셔너리 저장소 생성
    for char in text: 
        result[char] = result.get(char, 0) + 1 # result에 단어가 생기면 key를 얻고 value +1
    
    for key in result: # result 에 있는 값을 key에 넣음
        print(key, result[key]) # key와 value 출력