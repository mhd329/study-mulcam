    
    
with open('C:/Users/이주현/Desktop/Samsung multicampus/project01/01-PJT-01/3회차/이주현/data/fruits.txt', 'r', encoding='utf-8') as f:
    texts = f.readlines()

    result = {}
    for text in texts:
        text = text[:-1]
        result[text] = result.get(text,0) + 1



        print(result)

with open ("03.txt.","w",encoding="utf-8") as file:
    for j in result:
        file.write(f"{j} {result[j]}\n")



    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #text1 = text.replace("\n", " ")
    #print(len(text1)) 