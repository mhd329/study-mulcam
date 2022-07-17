fruit = open("data/fruits.txt","r",encoding="UTF-8")
count= 0
'''for i in fruit :
    if i[-6:] == 'berry\n' :
        count=count+1
print(count)
print(i[-6:])'''

result=[]
for i in fruit:
    if i.endswith('berry\n') == True :
        count = count+1
        for vaule in i:
           if vaule not in result:
                result.append(vaule)
        print(result)
print(count)


