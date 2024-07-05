with open('data\\fruits.txt' , 'r',encoding='utf-8') as f:
    f_list=set(f.read().splitlines()) # 중복제거,\n이 제거된 문자열 리스트 리턴
    berry_list=[]
    cnt = 0 # 'berry' 수만큼 카운트 변수 선언 0으로 초기화
    for name in f_list:
        if name[-5:] == 'berry': #문장의 끝에 berry 가 있어야 하기때문에 인덱스를 음수기호를 붙여 사용//berryFake가 존재함.   
            berry_list.append(name)
            cnt+=1
    
    print(cnt)
    print(berry_list)
with open('02.txt', 'w',encoding='utf-8') as f:
   
    f.write(f'{cnt}\n')
    f.writelines('\n'.join(berry_list))