with open('fruits.txt', 'r', encoding= 'utf-8') as f :
    fruit = f.readlines()

    fruits = []
    
    for i in fruit :
        i = i.strip('\n')
        fruits.append(i)
    
    berry_dic = {}

    for i in fruits :
        if i.endswith('berry') :

           berry_dic[i] = fruits.count(i)
    
    cnt = 0

    for k in berry_dic.keys() :

        cnt += 1

    print(cnt)

    for k in berry_dic.keys() :

        print(k)