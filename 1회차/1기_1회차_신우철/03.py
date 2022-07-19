import re
import string
with open('data/fruits.txt','r',encoding='utf-8') as f:
    frequency = {}
    text_string = f.read().lower()
    match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
 
    for word in match_pattern:
        count = frequency.get(word,0)
        frequency[word] = count + 1
     
    frequency_list = frequency.keys()
 
    for words in frequency_list:
        print(words, frequency[words])