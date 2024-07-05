f=open("C:\\Users\\user\\Desktop\\01-PJT-01\\2회차\\지현식\\data\\fruits.txt","r",encoding="UTF8")

target="berry"
answer=[]

lines = f.readlines()
lines = [line.rstrip('\n') for line in lines]

for a in lines:
    if target in a:
        if target in a[-(len(a)//2+1):]:
            if not a in answer:
                answer.append(a)
print(len(answer))
for i in answer:
    print(i)