from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
import repositories.city_repository as city_repository

cities_blueprint = Blueprint("cities", __name__)

# INDEX - no need to see all cities together
# select_all_cities_by_counrty_id
@cities_blueprint.route("/cities")
def cities(counrty_id):
    
    return render_template("cities/index.html", cities = cities)

