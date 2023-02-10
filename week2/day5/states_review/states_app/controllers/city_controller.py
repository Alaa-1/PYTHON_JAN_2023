from flask import render_template, redirect, request
from states_app import app
from states_app.models import city_model

# ======= Display Route ========
@app.route("/cities")
def show_all_cities():
    all_cities = city_model.City.fetch_all()
    return render_template("all_cities.html", all_cities=all_cities)