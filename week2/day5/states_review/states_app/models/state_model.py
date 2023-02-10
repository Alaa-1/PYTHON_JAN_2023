from states_app.config.mysqlconnection import connectToMySQL
from states_app import DATABASE

class State:
    def __init__(self, data):

        self.id = data['id']
        self.name = data['name']
        self.population = data['population']
        self.area = data['area']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    
    # ineract w/ the DATABASE

    # ======= READ ALL ========
    @classmethod
    def fetch_all(cls):

        q = """
            SELECT * FROM states;
            """
        result = connectToMySQL(DATABASE).query_db(q)
        
        these_states = []
        
        for row in result:
            this_state = cls(row)

            these_states.append(this_state)

        print(these_states)
        return these_states
    
    # ======= SAVE ========
    @classmethod
    def save(cls, data):

        q = """
            INSERT INTO states (name, population, area, created_at, updated_at)
            VALUES (%(name)s, %(population)s, %(area)s, NOW() , NOW())
            """
        
        result = connectToMySQL(DATABASE).query_db(q, data)

        return result
    

    # ======= SHOW ONE BY ID ========

    @classmethod
    def get_one_by_id(cls, data):

        query = """
                SELECT * FROM states
                WHERE id = %(id)s;
                """
        result = connectToMySQL(DATABASE).query_db(query,data)
        this_state = cls(result[0])
        return this_state