# 하단의 내용을 00.txt에 기록하시오.
# N회차 홍길동
# Hello, Python!
# 1일차 파이썬 공부 중
# 2일차 파이썬 공부 중
# 3일차 파이썬 공부 중
# 4일차 파이썬 공부 중
# 5일차 파이썬 공부 중

# 파일 생성하기
f = open("00.txt", 'w')

# 내용 입력
f.write('2회차 이상용\n')
f.write('Hello, Python!\n')
for i in range(1,6):
    data = '%d일차 파이썬 근무중\n' % i
    f.write(data)

# 파일 닫기
f.close()

