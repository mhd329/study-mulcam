f=open("C:\\Users\\user\\Desktop\\01-PJT-01\\2회차\\지현식\\00","w")
f.write("2회차 지현식\n")
f.write("Hello,Python!\n")

for i in range(1,6):
    data="%d일차 파이썬 공부 중\n" %i
    f.write(data)
f.close()