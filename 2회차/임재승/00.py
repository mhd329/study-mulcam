# 쓰기방식 파일 00.txt
f = open('00.txt', 'w', encoding='UTF8')
# write로 f에 값을 넣어준다.
f.write('2회차 임재승\n')
f.write('Hello, Python!\n')

# for문을 이용해 f에 값을 넣어준다.
for i in range(1, 6):
    f.write(f'{i}일차 파이썬 공부중\n')

# 닫는다.
f.close