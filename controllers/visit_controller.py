from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.visit import Visit
import repositories.visit_repository as visit_repository
import repositories.city_repository as city_repository
import repositories.user_repository as user_repository
import repositories.country_repository as country_repository
import pdb

visits_blueprint = Blueprint("visits", __name__)


@visits_blueprint.route("/visits")
def visits():
    visits = visit_repository.select_all()
    return render_template("visits/index.html", visits = visits)

#NEW 
@visits_blueprint.route("/visits/new")
def new_visit():
    users = user_repository.select_all()
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    return render_template("visits/new.html", users = users, countries = countries, cities = cities)


#CREATE - POST
@visits_blueprint.route("/visits", methods=["post"])
def create_visit():
    user_id = request.form["user_id"]
    city_id = request.form["city_id"]
    visited = request.form["visited"]
    user = user_repository.select(user_id)
    city = city_repository.select(city_id)
    visit = Visit(user,city,visited)
    visit_repository.save(visit)
    return redirect("/visits")


#DELETE
@visits_blueprint.route("/visits/<id>/delete", methods=["post"])
def delete_visit(id):
    visit_repository.delete(id)
    return redirect("/visits")

#EDIT
@visits_blueprint.route("/visits/<id>/edit")
def edit_visit(id):
    visit = visit_repository.select_visit(id)
    users = user_repository.select_all()
    cities = city_repository.select_all()
    return render_template("/visits/edit.html", visit = visit, users = users, cities = cities)

#EDIT - UPDATE
@visits_blueprint.route("/visits/<id>", methods=["post"])
def update_visit(id):
    user_id = request.form["user_id"]
    city_id = request.form["city_id"]
    visited = request.form["visited"]
    user = user_repository.select(user_id)
    city = city_repository.select(city_id)
    visit = Visit(user, city, visited, id)
    visit_repository.update(visit)
    return redirect("/visits")





    

