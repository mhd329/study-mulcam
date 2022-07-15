f = open("data\\fruits.txt",'r')
tmp = f.readlines()
count =0
for item in tmp:
    print(item)
    count+=1
w = open("01.txt",'w')
w.write(str(count))
f.close()
