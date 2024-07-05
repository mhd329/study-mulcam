f = open("/Users/imac01/Desktop/multicampus/01-PJT-01/3회차/김태형/data/fruits.txt",'r')
fruit_list = f.readlines()
fruit_list_s = list(set(fruit_list))
berry_count=-1
berry_list=[]
for i in fruit_list_s:
    if "berry" in i:
        berry_count+=1 # 1 더 크게 나온 이유 :
        berry_list.append(i)
f02 = open("/Users/imac01/Desktop/multicampus/01-PJT-01/3회차/김태형/02.txt",'w')
f02.write(str(berry_count))
f02.write('\n')
for i in berry_list:
    f02.write(i)
f02.close()