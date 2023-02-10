from flask import render_template, redirect, request
from states_app import app
from states_app.models import state_model

# ====== Display Route ========
@app.route("/states")
def show_all_states():
    us_states = state_model.State.fetch_all()

    return render_template("all_states.html", us_states = us_states)


# ====== Display Route ========
@app.route("/states/form")
def show_state_form():

    return render_template("create_state.html")

# ====== Action Route ========
@app.route('/states/add', methods=['post'])
def process_state_form():
    # data = {
    #     'name': request.form['name'],
    #     'population': request.form['population'],
    #     'area': request.form['area']
    # }
    state_id = state_model.State.save(request.form)

    return redirect("/states")

# ====== Display Route ========
@app.route('/states/<int:id>/show')
def show_one_state(id):
    data = {'id':id}
    state = state_model.State.get_one_by_id(data)

    return render_template("show_one_state.html", state= state)