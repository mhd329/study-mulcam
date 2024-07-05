cnt = 0
berry = []
res = []

with open('data/fruits.txt', 'r', encoding='utf-8') as f:

    for i in f: # 수정 완료... 그냥 내가 실수하고 있었다.
        line = i.strip()
        if line.endswith("berry"):
            berry.append(line)
        
    berry_list = list(set(berry))
    
    for j in berry_list:
        res.append(j)
        cnt += 1

with open('test02.txt', 'w', encoding='utf-8') as br:
    
    br.write(f'{cnt}\n')
    for i in res:
        br.write(f'{i}\n')