from db.run_sql import run_sql
from models.city import City
import repositories.country_repository as country_repository

# save(city)
def save(city):
    sql = "INSERT INTO cities (name, country_id) VALUES (%s, %s) RETURNING id"
    values = [city.name, city.country.id]
    results = run_sql(sql, values)
    city.id = results[0]["id"]

# select_all()
def select_all():
    sql = "SELECT * FROM cities"
    cities = []
    results = run_sql(sql)
    for result in results:
        country = country_repository.select(result["country_id"])
        city = City(result["name"], country, result["id"])
        cities.append(city)
    return cities

# select(id)
def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        country = country_repository.select(results[0]["country_id"])
        city = City(results[0]["name"], country, results[0]["id"])
    return city

# delete_all()
# delete(id)
# update(city)
# select_users_who_visited(city)