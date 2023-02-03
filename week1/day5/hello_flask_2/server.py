from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/hello/<name>/<color>/<int:user_id>')          # The "@" decorator associates this route with the function immediately following
def hello_world(name, color, user_id):

    return render_template("hello.html", name = name, color = color, user_id = user_id) 

@app.route("/students")
def show_students():

    students_list = [
        {'name' : 'Michael', 'age' : 35},
       {'name' : 'John', 'age' : 30 },
       {'name' : 'Mark', 'age' : 25},
       {'name' : 'KB', 'age' : 27}
    ]

    return render_template("students.html", students = students_list)



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module   

    app.run(debug=True)    # Run the app in debug mode.

