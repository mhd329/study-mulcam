with open(r"data/fruits.txt",'r',encoding='utf-8') as f:
    datas = f.read()

cnt=0
data_list = datas.split('\n')
for i in data_list:
    cnt+=1

with open('01.txt', 'w', encoding='utf-8') as f:
    f.write(str(cnt))