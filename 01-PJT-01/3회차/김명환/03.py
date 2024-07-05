with open('data\\fruits.txt' , 'r',encoding='utf-8') as f:
    f_list=f.read().splitlines()
    dic = {}
    for name in f_list:
        if name in dic:
            dic[name] +=1
        else :
            dic[name] = 1       
    for key,value in dic.items():
        print(key,value)        
with open('03.txt', 'w',encoding='utf-8') as f:
    for key, value in dic.items():
        f.write((f'{key}:{value}\n'))
