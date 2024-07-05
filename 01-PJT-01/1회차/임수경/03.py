f = open(r'C:\Users\LGE\Desktop\01-PJT-01\1회차\임수경\data\fruits.txt', 'r', encoding="UTF-8")
text = f.read()
words = text.split()
word_counts = dict()

for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1    
for word, count in word_counts.items():
    print(word, count)
 
with open('03.txt', 'w', encoding='utf-8') as f:
    f.write(str(word, count) + '\n')


# 다른 예제 코드 참고하기 
# strip_lst = []
# fruit_dic = {}
# with open('data/fruits.txt','r', encoding='utf-8') as f:
#     full_data = f.readlines()
#     for text in full_data:
#         strip_lst.append(text.rstrip()) 
#     for fruit in strip_lst:
#         if fruit not in fruit_dic:
#             fruit_dic[fruit] = 1
#         else:
#             fruit_dic[fruit] += 1
# with open('03.txt', 'w', encoding='utf-8')as f:
#     for name in fruit_dic:
#         k = name
#         v = fruit_dic[name]
#         f.write(str(k)+' '+str(v)+'\n')