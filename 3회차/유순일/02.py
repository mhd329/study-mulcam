# 이태극님 코드 참고 / 코드를 보면서 주석으로 코드에 대한 것을 씀.
with open('./data/fruits.txt', 'r',encoding="utf-8") as f:
    text=f.read()
    fruit=text.split("\n")  # 한 단어씩 한줄한줄이니 \n을 split로 나눠줌.
    #fruit=text
    result=[]               # for문 이하의 알고리즘의 결괏값을 모으는 코드.
    cnt=0
    #print(lines)
    for i in fruit:
        if i.endswith("berry") or i.endswith(" berry"):     # 뒤에 오는 문자열(endswith)이 'berry' or ' berry'인지 확인. 
            cnt += 1                                        # if에서 값이 맞다면 cnt에 1씩 더 해줘.                                              
            if i in result:                                  
                continue                                    # result안에 그냥 문자열은 건너뛰어.
            else:
                result.append(i)                            # result안에 [i]에 해당한다면 result에 먼저 써진 '[i]의 개수' 다음으로 값을 추가해.
    print(len(result))                                      # result에 있는 문자열들의 개수를 프린트해.
    
    with open('02.txt', 'w', encoding="utf-8") as a:
        a.write(str(len(result))+"\n")                      # result 값에 넣은 것들의 개수를 02.txt에 써라.
        for x in range(len(result)):                        # 그리고 result에 들어간 값들을 02.txt에 써라.
            a.write(result[x]+"\n")