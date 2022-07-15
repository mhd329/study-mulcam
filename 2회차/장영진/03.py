import pprint
with open('data/fruits.txt', 'r', encoding='utf-8') as r:
    text = r.read()
    names = text.split('\n')

dic = {}

for name in names:
    if name in dic:
        dic[name] += 1
    else:
        dic[name] = 1

pprint.pprint(dic)

# 1. 이름과 등장 횟수를 저장할 비어있는 dic 생성
# 2. 리스트에 하나씩 꺼내 dic에 입력
# 3. 만약 dic에 이미 존재한다면 값을 증가
# 4. 없다면 이름과 값 1을 입력
# 5. 리스트가 끝날 때까지 반복
# 6. pprint 함수를 이용해 가독성좋게 출력