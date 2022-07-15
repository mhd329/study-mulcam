with open("./data/00.txt", 'w', encoding="utf-8") as f:
    l = ["  N회차 홍길동,        \
            Hello, Python!,      \
            1일차 파이썬 공부 중, \
            2일차 파이썬 공부 중, \
            3일차 파이썬 공부 중, \
            4일차 파이썬 공부 중, \
            5일차 파이썬 공부 중"]

    f.write(l[0].replace(" ", "").replace(",", "\n"))