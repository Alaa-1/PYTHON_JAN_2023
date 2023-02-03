from flask import Flask, render_template, request, redirect, session


app = Flask(__name__)
app.secret_key = "46413198416132189"

#* Show the form
@app.route("/")
def home():
    return render_template("form.html")

# * process the form - REDIRECT
@app.route("/process", methods= ["POST"])
def create_ninja():
    print(f"this the form info: {request.form}")

    session["name"] = request.form["ninja_name"]
    session["weapon"] = request.form["weapon"]
    session["rank"] = request.form["rank"]

    print(">>>> credit card purchase is done !")
    # ! never ever ever render on POST
    return redirect("/display")

    # Show the display page

@app.route("/display")
def show_page():
    print(f" ************{session}")
    return render_template("display.html")


@app.route("/logout")
def loggout():
    session.clear()
    return redirect("/")

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.




  