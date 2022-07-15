f=open("C:\\Users\\user\\Desktop\\01-PJT-01\\2회차\\지현식\\data\\fruits.txt","r")
cnt=0
while True:
    line = f.readline()
    if not line:break
    cnt+=1
print(cnt)
f.close()