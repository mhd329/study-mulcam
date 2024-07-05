with open("00.txt",'w',encoding='utf-8') as f:
    f.write("3회차 황수홍\nHello, Python!\n")
    for i in range(1,6):
        f.write(f"{i}일차 파이썬 공부중\n")