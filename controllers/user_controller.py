from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.user import User
import repositories.user_repository as user_repository

users_blueprint = Blueprint("users", __name__)

# INDEX
@users_blueprint.route('/users')
def users():
    users = user_repository.select_all()
    return render_template("users/index.html", users = users)

# DELETE
@users_blueprint.route('/users/<id>/delete', methods = ["POST"])
def delete(id):
    user_repository.delete(id)
    return redirect("/users")


#NEW
@users_blueprint.route('/users/new')
def new_user():
    return render_template("users/new.html")

#CREATE
@users_blueprint.route("/users", methods=["POST"])
def create_user():
    user_name = request.form["name"]
    new_user = User(user_name)
    user_repository.save(new_user)
    return redirect("/users")

#EDIT
@users_blueprint.route('/users/<id>/edit')
def edit_user(id):
    user = user_repository.select(id)
    return render_template('users/edit.html', user = user)

#UPDATE
@users_blueprint.route('/users/<id>', methods = ["POST"])
def update_user(id):
    name = request.form["name"]
    user = User(name, id)
    user_repository.update(user)
    return redirect("/users")

#SHOW - not used
@users_blueprint.route('/users/<user_id>')
def show_cities(user_id):
    user = user_repository.select(user_id)
    cities = user_repository.select_cities(user_id)
    return render_template("users/show.html", user = user, cities = cities)

