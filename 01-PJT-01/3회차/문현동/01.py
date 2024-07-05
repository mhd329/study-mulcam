import os

cnt = 0
with open(os.getcwd()+"\\data\\fruits.txt", 'r', encoding = "utf-8") as file:
    text = file.read()
    fruits_list = text.split("\n")
    
    for i in range(len(fruits_list)):
        cnt += 1
        
with open("01.txt", 'w', encoding = "utf-8") as file:
    file.write(str(cnt))