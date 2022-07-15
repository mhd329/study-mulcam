names=['berry', 'sort', 'berry1']

cnt = 0
result = []
for i in names:
    print(i)
    if 'berry' in i:
        cnt += 1
        result = i
            
print(cnt, result)