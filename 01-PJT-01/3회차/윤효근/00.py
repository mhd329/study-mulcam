f = open("00.txt",'w')
f.write("3회차 윤효근\nHello, Python!\n")
for i in range(1,6):
    f.write("%d일차 파이썬 공부 중\n"%i)

f.close()