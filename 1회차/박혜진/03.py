with open('fruits.txt', 'r', encoding= 'utf-8') as f :
    fruit = f.readlines()

    fruits = []
    
    for i in fruit :
        i = i.strip('\n')
        fruits.append(i)

    fruits_dic = {}

    for i in fruits :

        fruits_dic[i] = fruits.count(i)

    for k, v in fruits_dic.items() :
        print('{} {}'.format(k, v))