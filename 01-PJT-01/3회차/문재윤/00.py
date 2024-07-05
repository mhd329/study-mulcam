
# data = open('00.txt', 'r', encoding="UTF8")
# contents = data.read()
# print(contents)
# data.close()
with open('00.txt', 'w', encoding='utf-8') as ff:
    ff.write(f'3회차 문재윤\nHello, Python!\n1일차 파이썬 공부 중\n2일차 파이썬 공부 중\n3일차 파이썬 공부 중\n4일차 파이썬 공부 중\n5일차 파이썬 공부 중')