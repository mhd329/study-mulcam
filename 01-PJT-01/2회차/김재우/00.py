with open('00.txt', 'w', encoding='utf-8') as f: # w 쓰기전용
    f.write('N회차 홍길동\n') #write 줄바꿈
    f.write('Hello, Python\n')
    for i in range(1, 6): # i = 1~ 6일차 반복
         f.write(f'{i}일차 파이썬 공부 중\n')