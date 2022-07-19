
# 불러와서 개행으로 split들을 나눔
with open ('./data/fruits.txt', 'r', encoding = 'utf-8') as b:
    p = b.read()
    fruits = p.split('\n')
    # 숫자는 겹치는 것이 있으면 cnt에 추가하는 식으로
    # 만약 berry로 끝난다 하면 chart 리스트에 넣어준다
    # for문 써서 안에 존재하면 적어주는 형식으로 작성
    cnt = 0
    chart = []
    for fruit in set(fruits):
        if fruit.endswith('berry'):
            cnt += 1
            chart.append(fruit)

with open ('02.txt', 'w', encoding = 'utf-8') as b:
    b.write(f'{cnt}\n')
    for u in chart:
        b.write(f'{u}\n')


        