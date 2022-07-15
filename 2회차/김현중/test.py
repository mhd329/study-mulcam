a = [{'k':12,'n':'rr'},{'k':14,'n':'ee'}]
b = {'k':21}
lst = [12,14]

for i in range(len(lst)):
    for j in a:
        if j['k'] == lst[i]:
            print(j['n'])
