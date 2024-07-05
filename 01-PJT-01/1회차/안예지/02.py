from typing import Text


with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    
    
    names = f.read().split('\n')
   

    cnt = 0
    berry = []
    new_list = []
    
    for n in names :
        if n[-len('berry')::1] == 'berry':
            
            berry += [n]
            for m in berry : 
                if m not in new_list : 
                    cnt += 1
                    new_list += [m]
                    
    with open('02.txt', 'w', encoding='utf-8') as f:
        f. write(f'{cnt}\n')
        f. writelines('\n'.join(new_list))
                    

    # 2. .endswith 메소드 사용하기
    # 값 초기화
    # cnt=0
    # berry = []
    # new_list=[]
    
    # for n in names :
    #     if n.endswith('berry'):
    #         # endswith : 특정 문자가 마지막에 오는 문자열 찾기
    #         berry += [n]
    #         for m in berry :
    #             # 중복문 제거, set()사용도 가능
    #             if m not in new_list : 
    #                 cnt += 1
    #                 new_list += [m]

    
            
            
             
        
    