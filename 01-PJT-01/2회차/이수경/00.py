with open('00.txt', 'w', encoding='utf-8') as f:
    name = '이수경'
    class_no = 2
    sen = 'Hello, Python!'
    f.write(f'{class_no}회차 {name}\n')
    f.write(sen+'\n')
    for N in range(1,6):
        if N == 5:
            f.write(f'{N}일차 파이썬 공부 중')
            break
        f.write(f'{N}일차 파이썬 공부 중\n')