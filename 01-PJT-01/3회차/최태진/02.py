#파일의 데이터를 줄 단위로 읽음
#공백이 있는 경우, .split으로 구분하여 
# 각 인덱스에 해당 단어가 있는지 확인

#find(찾을문자, 찾기시작할위치)
#중복
cnt = 0
t_list = []
with open('fruits.txt','r',encoding = 'utf-8') as f:
    for line in f:
        if line.find('berry') != -1 : #문자열에 berry가 포함되어있다면
            line = line.rstrip()
            if line == 'berryfake':
                continue
            if line not in t_list: 
                t_list.append(line)
                cnt += 1

print(cnt)
print(t_list)
with open('02.txt','w', encoding = 'utf-8') as f:
    f.write(f'{len(t_list)}\n')
    for char in t_list :
        f.write(f'{char}\n')

