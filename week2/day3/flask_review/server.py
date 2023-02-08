from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'sdfazefcv erfadvsgfz 687465132' # set a secret key for security purposes


# @app.route('/')          # The "@" decorator associates this route with the function immediately following
# def hello_world():
#     return 'Hello World!'  # Return the string 'Hello World!' as a response




#* Display Route for FORM
@app.route('/movies/new')
def show_form():
    return render_template("form.html")

#? Action Route
@app.route("/movies/create", methods=['post'])
def process_form():
    # print(request.form)
    session['title']= request.form['title']
    session['year']  = request.form['year']
    session['genre']=  request.form['genre']
    session['rating'] = request.form['rating']

    print(f" ******* {session} *********")
    return redirect("/display_movie")
    
#* Display Route
@app.route("/display_movie")
def display():
    movies = [{
        "name": "007",
        "year": 2022
    },
    {
        "name" : "Avatar",
        "year": 2023
    },
    {
        "name": "unknown",
        "year": "N/A"
    }
    ]
    return render_template("show_one_movie.html", movie_list = movies )

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.