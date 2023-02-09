from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

from flask_app.models import movie_model

class Award:
    def __init__(self, data):
        self.id = data['id']
        self.award_name = data['award_name']
        self.created_at = data['created_at']
        self.updated_at= data['updated_at']
        self.movie_id = data['movie_id']
        self.recieved = []
    # =========== CREATE ===========

    @classmethod
    def create_award(cls, data):
        
        query = """
                INSERT INTO awards (award_name, movie_id)
                VALUES (%(award_name)s, %(movie_id)s);
                """
        
        return connectToMySQL(DATABASE).query_db(query, data)
    

    @classmethod 
    def get_all_awards(cls):

        query= """
                SELECT * FROM awards
                JOIN movies
                ON awards.movie_id = movies.id;
                """
        all_awards = []        
        result  = connectToMySQL(DATABASE).query_db(query)
        # print(result)
        if result:
            for row in result:
                this_award = cls(row) # create the award
                # fix the movie ambiguity 
                # prepare the data for the constructor
                movie_data ={
                    'id': row['movies.id'],
                    'title': row['title'],
                    'release_date': row['release_date'],
                    'description': row['description'],
                    'created_at': row['movies.created_at'],
                    'updated_at': row['movies.updated_at']
                }

                this_movie = movie_model.Movie(movie_data)
                this_award.recieved = this_movie
                all_awards.append(this_award)
                
        print(all_awards)

        return all_awards

        



        
     