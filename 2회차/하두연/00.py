# 'r' : read (읽기 전용)
# 'w' : write (쓰기 전용 - 덮어씀)
# 'a' : append (쓰는데 파일 있으면 이어서 씀)

with open('00.txt', 'w', encoding='utf-8') as f:
    f.write('2회차 하두연\n')
    f.write('Hello, Python!\n')
    for i in range(1,6):
        f.write(f'{i}일차 파이썬 공부 중\n')

    