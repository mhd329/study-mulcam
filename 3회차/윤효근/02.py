
# from collections import OrderedDict


# f = open("data\\fruits.txt",'r')
# w=open("02.txt",'w')
# tmp = f.readlines()
# a = ''.join(OrderedDict.fromkeys(tmp))
# count =0
# for word in a:
#     print()
#     if word.find("berry")>0:
#         print(word)
    
# w.write(str(count))



from collections import OrderedDict


f = open("data\\fruits.txt",'r')
w=open("02.txt",'w')
tmp = f.readlines()
my_set = set(tmp)
my_list = list(my_set)
result =[]
count =0
for word in my_list:
    if word.find("berry")>0:
        print(word)
        count+=1
        result.append(word)
    
w.write(str(count)+'\n')
for item in result:
    w.write(item)
