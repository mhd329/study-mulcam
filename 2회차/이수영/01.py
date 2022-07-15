with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
count = 0
fruits = text.split('\n') # f 리스트안 객체의 모든 빈공간 제거
for i in fruits:
    count += 1



with open('01.txt', 'w', encoding='utf-8') as f:
    f.write(str(count))