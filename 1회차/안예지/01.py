with open('data/fruits.txt', 'r', encoding='utf-8') as f :
    
    names = f.read().split('\n')
    
    cnt = 0
    
    for i in names:
        cnt += 1
with open('01.txt','w' , encoding='utf-8') as f :
    f. write(f'{cnt}')
       
 
    
  
       