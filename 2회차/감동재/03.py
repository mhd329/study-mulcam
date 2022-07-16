# string[-num:]
OutputDic = {} 

lines = " "

with open('C:/Users/rkaeh/Desktop/01-PJT-01/2회차/감동재/data/fruits.txt','r',encoding = 'utf-8') as f:
    while lines != "":
        lines = f.readline()
        if (lines not in OutputDic) and lines!="" :
            OutputDic[lines] = 0
        if lines != "" :
            OutputDic[lines] += 1

for o in OutputDic:
    print( o[0:len(o)-1] +" "+str(OutputDic[o]))



with open('C:/Users/rkaeh/Desktop/01-PJT-01/2회차/감동재/03.txt','w',encoding = 'utf-8') as f:
    for o in OutputDic:
        f.write(o[0:len(o)-1] +" "+str(OutputDic[o])+"\n")

