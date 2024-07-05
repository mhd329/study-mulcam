with open ('data/fruits.txt' , 'r' , encoding = 'utf-8') as f:
    lines = f.readlines()
    result = {}


    for a in lines:
        new = a.strip('\n')
        if not new in result:
            result[new] = 1
        
        else: result[new] += 1


with open ('03.txt' , 'w' , encoding = 'utf-8') as f:
    object = []
    
    for b in result :
        object.extend([b +' '+ str(result[b])])
    for c in object :
        f.write(c+'\n')       
    
        
