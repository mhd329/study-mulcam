import os

fruits_dict = {}

with open(os.getcwd()+"\\data\\fruits.txt", 'r', encoding = "utf-8") as file:
    
    text = file.read()
    fruits_list = text.split("\n")
    
    for fruit in fruits_list:
        if fruit in fruits_dict:
            fruits_dict[fruit] += 1
        else:
            fruits_dict[fruit] = 1
            
with open("03.txt", 'w', encoding = "utf-8") as file:
    
    for fruit in fruits_dict:
        file.write(f"{fruit} ")
        file.write(f"{fruits_dict[fruit]}\n")