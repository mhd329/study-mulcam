f=open("C:\\Users\\user\\Desktop\\01-PJT-01\\2회차\\지현식\\data\\fruits.txt","r")
f1=open("C:\\Users\\user\\Desktop\\01-PJT-01\\2회차\\지현식\\01.txt","w")
cnt=0
while True:
    line = f.readline()
    if not line:break
    cnt+=1
f1.write(str(cnt))

f.close()
f1.close()