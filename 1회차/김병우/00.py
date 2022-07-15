# N회차 김병우
# Hello, Python!
# 1일차 파이썬 공부 중
# 2일차 파이썬 공부 중
# 3일차 파이썬 공부 중
# 4일차 파이썬 공부 중
# 5일차 파이썬 공부 중

with open('00.txt', 'w', encoding='utf-8') as f:
    f.write('N회차 김병우\n')
    f.write('Hello, Python!!\n')
    for i in range(1, 6):
        f.write(f'{i} 일차 파이썬 공부 중\n')