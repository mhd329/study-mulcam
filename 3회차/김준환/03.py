strip_lst = []
fruit_dic = {}
with open('data/fruits.txt','r', encoding='utf-8') as f:
    full_data = f.readlines()
    for text in full_data:
        strip_lst.append(text.rstrip()) 
    for fruit in strip_lst:
        if fruit not in fruit_dic:
            fruit_dic[fruit] = 1
        else:
            fruit_dic[fruit] += 1
with open('03.txt', 'w', encoding='utf-8')as f:
    for name in fruit_dic:
        k = name
        v = fruit_dic[name]
        f.write(str(k)+' '+str(v)+'\n')