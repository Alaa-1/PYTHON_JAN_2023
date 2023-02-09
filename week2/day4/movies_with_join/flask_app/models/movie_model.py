from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
# model the class after the movies table from our database

from flask_app.models import award_model

class Movie:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.release_date = data['release_date']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.awards = []

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):

        query = "SELECT * FROM movies;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        result = connectToMySQL(DATABASE).query_db(query)
        movie_list = []
    
        for row in result:
            one_movie = cls(row)
            movie_list.append(one_movie)

        return movie_list

    # this method saves movies to DB
    @classmethod
    def save(cls, data):

        q = """
            INSERT INTO movies (title, release_date, description, created_at, updated_at )
            VALUES (%(title)s, %(release_date)s, %(description)s, NOW() , NOW());
            """
        result = connectToMySQL(DATABASE).query_db(q, data)
        print(f" ******** {result} ********")
        return result


    # # this method will fetch one movie by id

    # @classmethod
    # def get_one_by_id(cls, data):

    #     query = "SELECT * FROM movies WHERE id= %(id)s"

    #     result = connectToMySQL(DATABASE).query_db(query, data)

    #     if result:

    #         movie = cls(result[0])
    #         return movie

    #     return []
    


    # this method will fetch one movie by id

    @classmethod
    def get_one_by_id(cls, data):

        # left join because some movie won't have awards

        query = """
                SELECT * FROM movies
                LEFT JOIN awards ON movies.id = awards.movie_id
                WHERE movies.id = %(id)s;
                """

        result = connectToMySQL(DATABASE).query_db(query, data)

        print(result)
        if result:
            this_movie = cls(result[0])
            these_awards = []
            for row in result:
                # ! format data for awards
                # prepare the dict for the constructor for Award
                award_data = {
                    'id': row['awards.id'],
                    'award_name': row['award_name']   ,
                    'created_at': row['awards.created_at'],
                    'updated_at' : row['awards.updated_at'],
                    'movie_id': row['movie_id']
                }
                # ! now we need to import our Award model to init it
                this_award = award_model.Award(award_data)
                these_awards.append(this_award)
            # ? creating a new attribute for the Dog instance
            this_movie.awards = these_awards

            return this_movie
        
        return []



    #TODO
    #! Create delete and update_one movie methods