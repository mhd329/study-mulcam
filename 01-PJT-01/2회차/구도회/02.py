with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    count=0   
    result=[]
    for i in f:
        if i[-6:-1] == 'berry':
            if i not in result:
                count += 1
                result.append(i)

with open('02.txt', 'w', encoding='utf-8') as f:
    f.write(f'{count}\n')
    for b in result:
        f.write(b)
    
 
    #lines = f.readlines()
    #result=[]
    #line = lines.split()
    #print(lines, type(lines))