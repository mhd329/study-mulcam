with open('data/fruits.txt','r', encoding = 'utf -8') as f:
   text = f.read()
   names = text.split('\n')
   print(len(names))
    