with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    list = text.split('\n')
    
    result = {}
    for i in list : 
        if not i in result : 
            result[i] = 1
        else : 
            result[i] += 1
    print(result)

with open('03.txt', 'w', encoding="utf-8") as f2 : 
    for k,v in result.items():
        f2.write(str(k)+" ")
        f2.write(str(v)+"\n")
