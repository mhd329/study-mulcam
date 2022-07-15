f_dict = {}

with open('data/fruits.txt','r',encoding='utf-8') as f:
    for i in list(f.read().split('\n')):
        f_dict[i] = f_dict.get(i,0)+1
    for k, v in f_dict.items():
        print(k, v)