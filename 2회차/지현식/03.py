f=open("C:\\Users\\user\\Desktop\\01-PJT-01\\2회차\\지현식\\data\\fruits.txt","r",encoding="UTF8")
f1=open("C:\\Users\\user\\Desktop\\01-PJT-01\\2회차\\지현식\\03.txt","w",encoding="UTF8")
target="berry"

lines = f.readlines()
lines = [line.rstrip('\n') for line in lines]

answer={}
for i in lines:
    answer[i]=0
for i in lines:
    answer[i]+=1
while True:
    for k,v in answer.items():
        f1.write(k)
        f1.write(" ")
        # data = "%d일차 파이썬 공부 중\n" % i
        data="%d\n" % v
        f1.write(data)

f.close()
f1.close()