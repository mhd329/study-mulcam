with open('./data/fruits.txt', 'r', encoding = 'utf-8') as f:
    a = f.read() 
    result = []
    result_dict = {}
    
    fruits = a.split('\n')
    for i in fruits:
        if (i in result_dict):
            result_dict[i] = result_dict[i] + 1    

        else:
            result_dict[i] = 1

with open('03.txt', 'w', encoding = 'utf-8') as f:
    
    for i in result_dict:
        f.write(i + ' ' + str(result_dict[i]) + '\n')
        
