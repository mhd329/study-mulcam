with open('00.txt', 'w', encoding = 'UTF-8') as f:
    data = 'N회차 홍길동\n'
    f.write(data)
    data = 'Hello, Python!\n' 
    f.write(data)
    for i in range(1, 6):
        data = f'{i}일차 파이썬 공부 중\n' 
        f.write(data)
 