with open('00.txt', 'w', encoding='utf-8') as f:
    f.write('2회차 이제준\nHello, Python\n')        
    for i in range(1, 6):                         # 범위 1 이상 6 이하
        f.write(f'{i}일차 파이썬 공부 중\n')        
            # f-string은 문자열 가장 앞에 'f'를 붙여주고, {}에 어떤 값을 {}이 위치한 자리에 표현할지 적어주면 된다.