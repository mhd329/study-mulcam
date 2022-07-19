f = open('./data/fruits.txt', 'r', encoding = 'utf-8')

f = f.read()
f = f.split()
# f = set(f)
dic = {}

# print(len(f))     # 100  여기서도 f = set(f) 였음
for i in f :             ## f= set(f)로 두고 계속 돌리니까 제대로 된 값이 안나오지..
    if i in dic :
        dic[i] += 1
        print(dic[i])
    else : 
        dic[i] = 1
        
# print(len(dic))  # 100

for i in dic :
    print(i, dic[i])
    
