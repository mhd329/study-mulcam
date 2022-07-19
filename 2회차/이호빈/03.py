from cgitb import text
from pprint import pprint
with open('2회차/2회차-이호빈/이호빈/data/fruits.txt', 'r', encoding= 'utf-8') as f:
    text = [line.rstrip('\n') for line in f]
    my_dict ={}
    for line in text:
        my_dict[line] = my_dict.get(line, 0) + 1

    pprint(my_dict)