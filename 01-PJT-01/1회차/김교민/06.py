import json
from operator import itemgetter
from os import rename
from pprint import pprint
with open('data/movies.json', 'r', encoding = 'utf-8') as f:
    with open('data/genres.json', 'r', encoding = 'utf-8') as g:
        a = json.load(f)
        b = json.load(g)
        n = {}
        result = []
        for c in b:
            n[c['id']] = c['name']
        for i in range(len(a)):
            name = []
            for g in a[i]['genre_ids']:
                name.append(n[g])
            a[i]['genre_names'] = name
        for h in a:
            re = {}
            re['genre_names'] = h['genre_names']
            re['id'] = h['id']
            re['overview'] = h['overview']
            re['title'] = h['title']
            re['vote_average'] = h['vote_average']
            result.append(re)
        pprint(result)