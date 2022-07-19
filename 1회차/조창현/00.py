f = open('data/00.txt', 'w')
f.close()
with open('data/00.txt', 'w', encoding = 'utf-8') as f:
    f.write('1회차 조창현\n')
    f.write('Hello, Python!\n')
    for i in range(0, 5):
        f.write(f'{i}일차 파이썬 공부 중\n')