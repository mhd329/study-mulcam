#과일 데이터 fruits.txt를 활용하여 berry로 끝나는 과일의 갯수와 목록을 02.txt  에 기록하시오.

with open('data/fruits.txt', 'r', encoding='utf-8') as f:

    text = f.read()
    result = text.split('\n')
    fruits1 = set(result)
    
    cnt = 0
    result = []

    for i in fruits1:
        if i.endswith('berry'):
            cnt += 1
            result += [i]
            

    print(cnt,result)
    
    
with open('02.txt', 'w', encoding='utf-8') as a:
    a.write(f'{cnt,result}')

            
    
       
   
   