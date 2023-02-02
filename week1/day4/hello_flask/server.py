from flask import Flask, render_template  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():

    return 'Hello World!'  # Return the string 'Hello World!' as a response


# @app.route("/dashboard")
# def dashboard():
#     print("Welcome to your Dashboard")
#     return ("Welcome to your Dashboardalert")


@app.route("/welcome")
def welcome():
    return render_template("index.html")

@app.route("/welcome/<my_name>/<int:times>")
def dashboard(my_name, times):
    print(type(times))
    return render_template("index.html", my_name = my_name, times = times)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

