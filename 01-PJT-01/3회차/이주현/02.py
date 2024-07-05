with open('C:/Users/이주현/Desktop/Samsung multicampus/project01/01-PJT-01/3회차/이주현/data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()     # 가져온 파일을 읽음
    fruits = text.split('\n')    #fruits을 리스트로 변환
    fruits1 = set(fruits)
    cnt = 0
    result = []
   # for i in fruits1:
      #  if 'berry' in i:
         #   cnt += 1
          #  result += [i]
           # result.append(i)
    
    print(cnt,result)


    for i in fruits1:
       if i.endswith('berry'): 
           cnt += 1
           result += [i]
    print(cnt,result)
    

  


  

    
    
    
    
    
    
    
    
    
  