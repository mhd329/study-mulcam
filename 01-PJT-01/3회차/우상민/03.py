import pprint
counter = {}
with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
       text = f. read()
       fruit1 = text.split('\n')
       for i in fruit1:
        try: counter[i] += 1
        except: counter[i] = 1 
       pprint.pprint(counter)