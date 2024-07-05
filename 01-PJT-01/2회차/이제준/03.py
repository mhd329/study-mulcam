with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    fruits = f.read().split('\n')

    dict = {}

for i in fruits:
    if i in dict:
        dict[i] += 1               # 이미 'i'가 'dict'에 존재하면 값에 1을 더해준다
    else:
        dict[i] = 1

for x, y in dict.items():     # .item()을 사용하여 dictionary의 key와 value를 출력할 수 있다
    print(x, y)


with open('03.txt', 'w', encoding='utf-8') as f:
    for x, y in dict.items():    
        f.write(f'{x} {y}\n')   # print 대신 f.write를 f-string을 사용해서 문자열 안에 변수를 넣어 준다