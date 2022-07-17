
# result = {}

# with open('data/fruits.txt' , 'r' , encoding='utf-8') as f:
#     text = f.read()
#     spt = text.split()
#     for y in spt:
        
#         if y in result:
#             result[y] = result[y] + 1
#         else:
#             result[y] = 1
     
# print(result)


result = {}

with open('data/fruits.txt' , 'r' , encoding='utf-8') as f:
    text = f.read()
    spt = text.split()
    for y in spt:
        result[y] = result.get(y,0) + 1
        


     
print(result)
    
    