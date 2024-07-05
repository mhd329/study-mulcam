# f에 data폴더 fruits 텍스트파일을 읽기방식으로 넣어준다.
f = open('./data/fruits.txt', 'r', encoding='UTF8')

# lines에 한줄씩 넣어준다.
lines = f.readlines()

# 개행을 제거해준다.
fruits = [fruit.strip() for fruit in lines]

# 어제한 예제와 동일...?
def duplication(n):
    # 빈 딕셔너리 선언
    diction = {}
    # 리스트에 있으면 1 더해주고 없으면 생성 후 1로 초기화
    for list in n:
        if list in diction:
            diction[list] += 1
        else:
            diction[list] = 1
    
    for key, value in diction.items():
        print(key, value)

duplication(fruits)