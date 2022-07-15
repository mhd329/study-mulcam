f=open("C:\\Users\\user\\Desktop\\01-PJT-01\\2회차\\지현식\\data\\fruits.txt","r",encoding="UTF8")

target="berry"
answer=[]

lines = f.readlines()
lines = [line.rstrip('\n') for line in lines]

answer={}
for i in lines:
    answer[i]=0
for i in lines:
    answer[i]+=1
for k,v in answer.items():
    print(k,v)