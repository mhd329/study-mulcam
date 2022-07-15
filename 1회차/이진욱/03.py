with open('data/fruits.txt', 'r',encoding='utf-8') as f:
    
    f_list=[]
    f_set=set()
    while True:
        text03 = f.readline().rstrip()
        if text03 == '':
            break
        f_list.append(text03)
        f_set.add(text03)    

    f_dic={}

    for i in range(len(list(f_set))):
        f_dic[list(f_set)[i]] = f_list.count(list(f_set)[i])
    
    print(f_dic)


    d= open('03.txt','w',encoding='utf-8')
    for i in f_dic.keys():
        d.write(f'{i} {f_dic[i]} \n')