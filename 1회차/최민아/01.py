f = open('data/fruits.txt', 'r', encoding='utf-8')
cnt = 0
while True:
    if f.readline() == '':
        break
    cnt += 1
f.close()

with open('01.txt', 'w', encoding='utf-8') as f:
    f.write(str(cnt)) 
    f.close()