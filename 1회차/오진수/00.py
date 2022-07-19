# 텍스트 데이터 출력 (연습)
#아래의 내용을  `00.txt`에 기록하시오.

with open('00.txt', 'w', encoding='utf-8') as f:
    f.write('N회차 홍길동\n')   #\n은 문자열 안에 들어가야 한다?
    f.write('Hello, Python!\n')

    
    for i in range(1,6):
        f.write(f'{i}일차 파이썬 공부 중\n')
