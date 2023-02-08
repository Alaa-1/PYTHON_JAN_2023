from flask import Flask, render_template, request, redirect # Import Flask to allow us to create our app
from movie_model import Movie
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def show_all():
    all_movies = Movie.get_all()
    print(all_movies)
    return render_template("movies.html", all_movies = all_movies)  # Return the string 'Hello World!' as a response

#* Display Route
@app.route("/movies/new")
def show_form():
    return render_template("movie_form.html")

#? Action Route
@app.route("/movies/create", methods=['POST'])
def process_form():

    data = {
        "title": request.form["title"],
        "release_date": request.form['release_date'],
        "description": request.form['description']
            }

    movie_id = Movie.save(data)

    return redirect(f"/movies/show/{movie_id}")

#* Display Route
@app.route("/movies/show/<int:id>")
def show_one_movie(id):

    data = {"id":id}
    one_movie = Movie.get_one_by_id(data)

    return render_template("one_movie.html", movie = one_movie)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.