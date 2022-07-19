with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
fruits = text.split('\n')
result = {}
for char in fruits:
    if not char in result:
        result[char] = 1
    else:
        result[char] = result[char] + 1 

with open('03.txt', 'w', encoding='utf-8') as f:
    for key, value in result.items():  # .items() : 딕셔너리의 모든 키-값의 상을 담은 뷰 반환
        f.write(f'{key}, {value}\n') 