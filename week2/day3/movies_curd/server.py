from flask import Flask, render_template  # Import Flask to allow us to create our app
from movie_model import Movie
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    all_movies = Movie.get_all()
    print(all_movies)
    return render_template("movies.html", all_movies = all_movies)  # Return the string 'Hello World!' as a response


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.