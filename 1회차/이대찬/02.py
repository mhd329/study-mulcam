with open('./data/fruits.txt', 'r', encoding = 'utf-8') as f:
    a = f.read() 
    result = []
    
    fruits = a.split('\n')
    for i in fruits:
        if ('berry' in i[len(i)-5:]):
            result.append(i)
result2 = str(len(set(result)))+'\n'

with open('02.txt', 'w', encoding = 'utf-8') as f:
         
    f.write(result2)
    for i in set(result):
        f.write(i+'\n')
        
 