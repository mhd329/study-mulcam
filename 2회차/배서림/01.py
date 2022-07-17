# 과일 데이터 `fruits.txt`를 활용하여 총 과일의 갯수를 `01.txt`  에 기록하시오.
# 과일은 하나당 한 줄에 기록되어 있습니다.


with open('data/fruits.txt', 'r', encoding = 'utf-8') as f: # f란 이름으로 fruits.txt를 읽기 전용으로 열 건데
    text = f.read() # 이 문자열(==text) 안의
    noblank = text.replace(' ', '') # 공백을 지우고(==noblank)
    fruits = noblank.split() # 이걸 리스트로 만들어서(==fruits)
    print(len(fruits)) # 이 리스트의 길이를 출력함


# output
# 394