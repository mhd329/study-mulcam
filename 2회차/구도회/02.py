with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    count=0
    fruits = list()
    for i in f:
        
        if i.endswith('berry'):
            count+=1
        print(count)        

    
    #lines = f.readlines()
    #result=[]
    #line = lines.split()
    #print(lines, type(lines))
    for line_1 in lines:
        if 'berry' in line_1:
            print(count)
            result=result.append(line_1)
   
