



    
with open('C:/Users/이주현/Desktop/Samsung multicampus/project01/01-PJT-01/3회차/이주현/data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.readlines()
    count = 0
    for i in text:
        if text != '':
            count +=1
  

    with open('01.txt','w', encoding='utf-8') as fi:
        fi.write(str(count))
    
    
    
    
  











