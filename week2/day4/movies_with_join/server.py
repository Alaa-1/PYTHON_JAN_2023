from flask_app import app
#! Always remember to import all the controllers
from flask_app.controllers import movie_controller
from flask_app.controllers import award_controller

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.