from mysqlconnection import connectToMySQL

# model the class after the movies table from our database

class Movie:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.release_date = data['release_date']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):

        query = "SELECT * FROM movies;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        result = connectToMySQL('movies_schema').query_db(query)
        print(f" ====== \n {result} \n ======== \n")
        movie_list = []
    
        for row in result:
            one_movie = cls(row)
            movie_list.append(one_movie)

        return movie_list




