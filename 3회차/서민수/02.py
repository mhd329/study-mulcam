f1 = open('02.txt', 'w', encoding='utf-8')


f = open('data/fruits.txt', 'r', encoding='utf-8')
text = f.read()
 
    
fr = text.split('\n')
berry = []
for i in fr:   
    if i.endswith("berry"):
       if not i in berry:
            berry.append(i)        
f1.write(str(len(berry)) + '\n')
for i in berry:
    f1.write(i+'\n')
f1.close()
f.close()