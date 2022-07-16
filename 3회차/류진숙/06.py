import json
from pprint import pprint



# 코드 진행방법
# movies 안의 movie 첫번째 중
# genre_ids의 밸류 값 [18, 80] 이 각각의 값에 넣고 싶다는 것

def movie_info(movies, genres):


    for movie in movies:  
        for mv in movie["genre_ids"]:
            a = []
            a.append(movie["genre_ids"])
            
            print(a)
            # name = []
            # name.append(movie["genre_ids"])
            # print(name)
            # for genre in genres:
            #     for a in name:
            #         if genre["id"] == a:
            #             a = []
            #             a.append(genre["name"])            

                
            
            
            # for genre in genres:
            #     if name == genre["id"]:
            #         a = []
            #         a.append(genre["name"])
            #         print(a)
                
            
        # for i in n:
        #     for genre in genres:
        #         if genre["id"] == i:
        #             a = []
        #             a.append(genre["name"])
        #             print(a)
                

            # for genre in genres:
            #     if genre["id"] == n:
                    

        # for genre in genres:
        #         if genre["id"] == n:
        #             a = []
        #             a.append(genre["id"])
        #             print(a)
              

                    
        # for genre in genres:
        #     if genre["id"] == name:
                
                    #     for genre in genres:
                    # if genre["id"] == mv:
                    #     name.append(genre["name"]) 
                    #     print(name)

    # name = []
    # for movie in movies:
    #     for a in movie:
    #         for genre in genres
            # for a in mv:
            #     print(a)
                # for genre in genres:
                #     if genre["id"] == mv:
        
                #         name.append(genre["name"])
                #         print(name)

    
    
    # final = []
    # name = []
    # for movie in movies:
    #     for h in range(len(movie["genre_ids"])):
    #         for genre in genres:
    #             if genre["id"] == movie[h]["genre_ids"]:
    #              print(h)            
                 #     if genre["id"] 

            # print(movie)
            # for a in movie:
                
            #         print(p)
            #                     # if genre["id"] == movie["genre_ids"][mv]:
                #     name.append(genre["name"])
                # print(name)
            # for genre in genres:
            #     if genre["id"] == mv:
            #         name.append(genre["name"])
            #         print(name)

                                                                           
    # for i in name:
    #     if movie["genre_ids"] == i:  
    #         result = {
    #         "genre_names": name,
    #         "id": movie.get("id"), 
    #         "title": movie.get("title"),
    #         "overview": movie.get("overview"),
    #         "title": movie.get("title"),
    #         "vote_average": movie.get("vote_average")
    #         }
    #     print(result)
    
    # final.append(result)

    # return final

    # 여기에 코드를 작성합니다.  

        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))