from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.visit import Visit
import repositories.visit_repository as visit_repository

visits_blueprint = Blueprint("visits", __name__)


#INDEX
@visits_blueprint.route("/visits")
def visits():
    visits = visit_repository.select_all()
    return render_template("visits/index.html", visits = visits)
