
from regex import I


with open('3.txt', 'w', encoding='UTF-8') as f:
    with open('data/fruits.txt','r', encoding='UTF=8') as f1:
        text = f1.readlines()
        my_dict = {}
        cnt = 0
        for i in text:
            if i not in my_dict:
                my_dict[i] = 0
            if i in my_dict:
                my_dict[i] += 1
    for key,value in my_dict.items():
        print(key.strip(),value)
        f.write(f'{key.strip()} ')
        f.write(f'{str(value)}\n')
