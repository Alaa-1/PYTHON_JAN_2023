from states_app.config.mysqlconnection import connectToMySQL
from states_app import DATABASE
from states_app.models import state_model

class City:
    def __init__(self, data):

        self.id = data['id']
        self.name = data['name']
        self.zip = data['zip']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.state_id = data['state_id']
        self.located = []

    @classmethod
    def fetch_all(cls):

        q = """
            SELECT * FROM cities
            LEFT JOIN states ON cities.state_id = states.id;
            """
        result = connectToMySQL(DATABASE).query_db(q)
        
        these_cities = []
        
        print(result)

        for row in result:
            this_city = cls(row)

            # fix the state ambiguity 
            # prepare the data for the constructor
            state_data = {
                'id': row['states.id'],
                'name': row['states.name'],
                'area': row['area'],
                'population': row['population'],
                'created_at': row['states.created_at'],
                'updated_at': row['states.updated_at']

            }

            this_state = state_model.State(state_data)
            this_city.located = this_state

            these_cities.append(this_city)

        return these_cities