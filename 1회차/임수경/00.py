# '00.txt' 파일 생성 
# w : write 쓰기 전용 
with open('00.txt', 'w', encoding = 'utf-8') as f:
    f.write('N회차 홍길동\n')             #f 라는 파일에 ()안에 들어있는 text를 작성할게
    f.write('Hello, Python!\n')           #\n , enter 효과
    f.write('1일차 파이썬 공부 중\n')
    f.write('2일차 파이썬 공부 중\n')
    f.write('3일차 파이썬 공부 중\n')
    f.write('4일차 파이썬 공부 중\n')
    f.write('5일차 파이썬 공부 중\n')

