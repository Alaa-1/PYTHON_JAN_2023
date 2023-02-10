from flask import Flask  # Import Flask to allow us to create our app
from states_app import app
from states_app.controllers import state_controller
from states_app.controllers import city_controller


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.