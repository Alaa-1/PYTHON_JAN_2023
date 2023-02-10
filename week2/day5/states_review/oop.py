

class State:
    def __init__(self, data):

        self.id = data['id']
        self.name = data['name']
        self.population = data['population']
        self.area = data['area']



class City:
    def __init__(self, data):
        self.id = data['id']
        self.city_name = data['city_name']
        self.zip = data['zip']
        self.state_id = data['state_id']



data = {
    'id':1,
    'name': 'California',
    'city_name': 'random_city',
    'population': 8529852,
    'area':798465132,
    'president':'Robert',
    'zip': 521864,
    'state_id': 3}

state1 = State(data)

city1 = City(data)


print(state1.name)