with open('data/fruits.txt', 'r', encoding='utf-8') as r:
    text = r.read()
    names = list(text.split('\n'))
    cnt = 0

berry = [] # berry로 끝나는 문자열 저장
for name in names:
    if name.endswith('berry'):
        berry.append(name)

berryList = [] # 중복 삭제된 리스트 저장
for i in berry:
    if i not in berryList:
        berryList.append(i)

print(len(berryList)) # berry로 끝나는 과일 갯수

for fruit in berryList: # berry로 끝나는 과일 목록
    print(fruit)