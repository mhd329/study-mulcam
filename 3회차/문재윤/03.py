
with open('data/fruits.txt', 'r', encoding="UTF8") as data:
    contents = data.read()
#print(type(contents))
    contents = (contents.split('\n'))

    dic = {}
    for words in contents:
        if words in dic:
            dic[words] +=1
        else:
            dic[words] = 1
    dic = list(dic.items())
    # for i in dic:
    #     print(type(i))
    #     i = str(i)
    #     i = i.replace("(","").replace(")","").replace("\'","").replace(",","")
    #     print(i)

    with open('03.txt','w',encoding='utf-8') as gg:
        for i in dic:
            i = str(i)
            i = i.replace("(","").replace(")","").replace("\'","").replace(",","")
            gg.write(i)
            gg.write('\n')

    # with open('03.txt', 'w', encoding='utf-8') as ff:

    # for key in list(dic.keys()):
    #     print(key ,dic[key])
    #     ff.write(f'{key ,dic[key]}')