import json
from pprint import pprint
with open('data/movie.json', 'r', encoding = 'utf-8') as f:
    a=json.load(f)
    result = {
        'genre_ids' : a.get('genre_ids'),
        'id' : a.get('id'),
        'overview' : a.get('overview'),
        'title' : a.get('title'),
        'vote_average' : a.get('vote_average')
    }
    pprint(result)