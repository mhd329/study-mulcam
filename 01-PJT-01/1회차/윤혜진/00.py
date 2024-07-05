# '00.txt' 파일 생성 후, 문자열 기록
with open('1회차/윤혜진/result/00.txt', 'w', encoding='utf-8') as f:
    f.write('N회차 윤혜진\n')
    f.write('Hello, Python!\n')
    for i in range(1,6):
        f.write(f'{i}일차 파이썬 공부 중\n')