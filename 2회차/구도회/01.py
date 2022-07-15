with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.readlines()
    count=0
    
       
    for fruits in text:
        count+=1
    print(count)       
 
with open('01.txt', 'w', encoding='utf-8') as f:
    f.write(str(count))