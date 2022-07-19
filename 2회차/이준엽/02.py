with open('data/fruits.txt','r',encoding='utf-8') as f:
    fruit = f.read()
    fruits = fruit.split('\n')
    berry=[]
    cnt=0
    for i in fruits :
        if i not in berry :
            if 'berry' in i[len(i)-5:len(i)]:
                    berry+=[i]
                    cnt+=1
    print(berry,cnt)

    # for i in fruits:
    #     if i not in berry :
    #         if i.endswith('berry') :
    #             berry+=[i]
    #             cnt+=1
    # print(berry,cnt)
    
with open('02.txt', 'w', encoding='utf-8')as f:
    f.write(f'{cnt}\n')
    for i in berry :
        f.write(f'{i}\n')