from flask_app import app
from flask import  render_template, request, redirect 

from flask_app.models.movie_model import Movie
from flask_app.models.award_model import Award


# Display Route
@app.route("/awards/new")
def display_award_form():
    all_movies = Movie.get_all()
    print(all_movies)
    return render_template("award_form.html", all_movies = all_movies)


# Action Route 
@app.route("/process", methods=['post'])
def give_award():
    Award.create_award(request.form)
    return redirect("/")

# Display Route

@app.route("/awards")
def show_awards():
    all_awards = Award.get_all_awards()
    
    return render_template("awards.html", awards = all_awards)