from tabnanny import check


with open(r"data/fruits.txt",'r',encoding='utf-8') as f:
    datas = f.read()

cnt=0
data_list = datas.split('\n')
new_list = []
for i in data_list:
    if i[-5:] == 'berry':
        new_list.append(i)

answer = set(new_list)

with open(r"02.txt", 'w', encoding='utf-8') as f:
    f.write(str(len(answer)))
    for i in answer:
        f.write(f"\n{i}")
# for j in range(0,len(new_list)-1):
#     for k in range(1,len(new_list)):
#         if new_list[i]==new_list[j]:
#             check_list=new_list[j]