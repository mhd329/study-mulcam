f1 = open('03.txt', 'w', encoding='utf-8')


f = open('data/fruits.txt', 'r', encoding='utf-8')
text = f.read()
 
    
fr = text.split('\n')
berry = dict()

for i in fr:   
    if not i in berry.keys():        
        berry[i] = 1
        
    else:
        berry[i] += 1
          
f1.writelines(str(berry)+'\n')

f1.close()
f.close()