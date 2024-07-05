# 00. 텍스트 데이터 출력 (연습)

with open('00.txt', 'w', encoding='utf-8') as f:
    f.write('2회차 김지연\n')
    f.write('Hello, python!\n')

    for i in range(1, 6):
        f.write(f'{i}일차 파이썬 공부 중\n')