result = []


with open('data/fruits.txt' , 'r' , encoding= 'utf-8') as y :
    text = y.read()
    w = text.split('\n')
    for z in w:
        if z.endswith('berry'):
            result.append(z)
    print(list(set(result)))    
          
            
    
            
