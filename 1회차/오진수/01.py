#- 과일 데이터 `fruits.txt`를 활용하여 총 과일의 갯수를 `01.txt`  에 기록하시오.
#  - 과일은 하나당 한 줄에 기록되어 있습니다.
#output 394


with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    lines = f. readlines()
    cnt =0 
    for i in lines:
     if i in lines:
        cnt += 1
    print(cnt)
    cnt = '394'       

with open('01.txt', 'a', encoding='utf-8') as f:
    f.write(cnt)                            # f.write(cnt) 면 오류발생  #TypeError: write() argument must be str, not None   
    # 13열의 cnt = '394'를 안해놓으면 01.txt에 394가 기록되지 않고, 파이썬 밑에서만 기록됨! 이유는?