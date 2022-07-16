import json
from pprint import pprint
with open('data/movie.json', 'r', encoding = 'utf-8') as f:
    with open('data/genres.json', 'r', encoding = 'utf-8') as g:
        a = json.load(f)
        b = json.load(g)
        name = []
        for c in a['genre_ids']:
            for i in range(0, len(b)):
                if b[i]['id'] == c:
                    name.append(b[i]['name'])
                
        result = {
            'genre_names' : name,
            'id' : a.get('id'),
            'overview' : a.get('overview'),
            'title' : a.get('title'),
            'vote_average' : a.get('vote_average')
        }
        pprint(result)