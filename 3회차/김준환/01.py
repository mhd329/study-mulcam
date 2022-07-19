with open('data/fruits.txt','r', encoding='utf-8') as f:
    cont = f.readlines()
    print(str(len(cont)))
with open('01.txt', 'w', encoding='utf-8')as f:
    f.write(str(len(cont)))
    
    # readline으로 구현시 문자열로 가져오는데 이때 짝수번만 가져오더라
    # for 문으로 구현 했는데 readlines를 for에서 쓰니 이유는 모르겠지만 첫 문장은 뛰어 넘더라 그래서 그냥 바로 길이를 구해서 출력