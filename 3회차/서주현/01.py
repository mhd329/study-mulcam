
f = open('./data/fruits.txt', 'r', encoding = 'utf-8')

ff = f.read()
ff = ff.split('\n')
print(len(ff))