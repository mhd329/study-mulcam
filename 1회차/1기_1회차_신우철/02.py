with open('data/fruits.txt','r',encoding='utf-8') as f:
    
    count = 0
    f = set(f)
    

    for line in f:
        
        words=line.split('\n')
            
        for word in words:
            
            if 'berry' in word:
                if word.endswith('berry'):
                    count += 1
                    print(word)
                
print(count)