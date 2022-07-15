with open('data/fruits.txt','r',encoding='utf-8') as f:
    text = f.read()
    names = text.split('\n')
    y = list(names)
    cnt = 0
    berry = []
    for i in y:
        if i.endswith("berry"):
            cnt +=1
            berry += [i]

import sys
sys.stdout = open('02.txt','w',encoding='utf-8') 

my_berry = set(berry)
my_list = list(my_berry)
print(len(my_list))
for i in my_list:
    print(i)
    


    
