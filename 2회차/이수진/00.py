with open("2회차/이수진/data/00.txt", 'a',encoding='utf=8') as f:
    f.write("2회차 이수진\n")
    f.write("Hello, Python!\n")
    for i in range(1,6):
        f.write(f'{i}일차 파이썬 공부 중\n')