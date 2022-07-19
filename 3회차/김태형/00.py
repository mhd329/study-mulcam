f = open("/Users/imac01/Desktop/multicampus/01-PJT-01/3회차/김태형/00.txt","w")
data01 = "3회차 김태형\nHello, Python!\n" 
f.write(data01)
for i in range(1,6):
    data02 = "%d일차 파이썬 공부 중\n" %i
    f.write(data02)
f.close()