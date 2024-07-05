from pprint import pprint
f = open("/Users/imac01/Desktop/multicampus/01-PJT-01/3회차/김태형/data/fruits.txt",'r')
f02 = open("/Users/imac01/Desktop/multicampus/01-PJT-01/3회차/김태형/03.txt",'w')
fruit_list = f.readlines()
fruit_set_list = list(set(fruit_list))
fruit_dict = {}
fruit_count = 0
for i in fruit_set_list:
    if i in fruit_list:
        fruit_dict[i]=fruit_list.count(i)
# fruit_list_2nd=[]
# for i in fruit_dict.keys():
#     for j in fruit_dict.values():
#         fruit_list_2nd.append(i,j)
pprint(fruit_dict)
# f02.write(str(fruit_dict))
# f02.close()