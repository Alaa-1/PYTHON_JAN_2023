# this model file interacts with the DB
# handle all data related to the table 'movies'

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

    #! all queries are classmethods
    # ========== READ ALL ===============
    @classmethod
    def get_all(cls):

        query = "SELECT * FROM movies;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        result = connectToMySQL('movies_schema').query_db(query)
        print(f" ====== \n {result} \n ======== \n")
        movie_list = []
        if result:

            for row in result:
                one_movie = cls(row)
                movie_list.append(one_movie)

            return movie_list

        return []

    # ============ CREATE ==============
    @classmethod
    def save(cls, data):

        q = """
        INSERT INTO movies (title, release_date, description, created_at, updated_at)
        VALUES (%(title)s, %(release_date)s, %(description)s, NOW(), NOW());
        """
        result = connectToMySQL('movies_schema').query_db(q, data)
        print(f" ******** {result} ********")
        return result


    # ========== READ ONE ===============
    @classmethod
    def get_one_by_id(cls, data):

        query = "SELECT * FROM movies WHERE id= %(id)s"
        
        result = connectToMySQL('movies_schema').query_db(query, data)

        if result:
            movie = cls(result[0])
            return movie
        return []
    

    #TODO
    #! Create delete and update_one movie methods