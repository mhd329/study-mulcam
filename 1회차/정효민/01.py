

from unittest import result


with open('data/fruits.txt' , 'r' ,encoding='utf-8') as y:
    text = y.read()
    w = text.split('\n')
    
    print(len(w))