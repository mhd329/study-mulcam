cnt = 0
lines= " "
with open('C:/Users/rkaeh/Desktop/01-PJT-01/2회차/감동재/data/fruits.txt','r',encoding = 'utf-8') as f:
    while lines != "":
        lines = f.readline()
        cnt+=1

    #루프에서는 lines = "" 일때도 카운트 했으니 -1 해주기
    cnt-=1
    
print(cnt) 

with open('C:/Users/rkaeh/Desktop/01-PJT-01/2회차/감동재/data/01.txt','w',encoding = 'utf-8') as f:
     f.write(str(cnt))
  