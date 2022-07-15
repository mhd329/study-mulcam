# fruits 불러오고 나누기
with open('data/fruits.txt', 'r', encoding='utf-8') as r:
    text = r.read()
    fruits = text.split('\n')

#berrylist에 berry로 끝나는 과일 저장
berrylist = []
for fruit in fruits:
    if fruit.endswith('berry'):
        berrylist.append(fruit)

#중복 제거
result = []
for i in berrylist:
    if i not in result:
        result.append(i)

with open('02.txt', 'w', encoding='utf-8') as f:
        f.write(f'{len(result)}\n')
        for i in result:
            f.write(f'{i}\n')