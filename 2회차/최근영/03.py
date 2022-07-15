with open(r"data/fruits.txt",'r',encoding='utf-8') as f:
    datas= f.read()


datas = datas.split('\n')
fruits_dict = {}
for i in datas:
    if i in fruits_dict:
        fruits_dict[i] += 1
    else:
        fruits_dict[i] = 1

with open('03.txt', 'w', encoding='utf-8') as f:
    for key,value in fruits_dict.items():
        f.write(f'{key} {value}\n')
