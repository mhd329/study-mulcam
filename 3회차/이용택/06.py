import json
from pprint import pprint

def movie_info(movies, genres):  

    result = []
    
    key_list = ['id', 'title', 'vote_average', 'overview', 'genre_names']

    for movie in movies:
        genre_ids = movie.get('genre_ids')
        genre_list = []
        for genre in genres:
            if genre['id'] in genre_ids:
                genre_list.append(genre['name'])
        elements = {}
        for key in key_list:
            elements[key] = movie.get(key,genre_list)  # 'NO RESULT' 대신에 장르 대응시켜야함 
        result.append(elements)
    return result



if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))