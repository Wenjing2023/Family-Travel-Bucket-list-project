from db.run_sql import run_sql
from models.city import City
from models.user import User
from models.visit import Visit
import repositories.country_repository as country_repository
import pdb

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

#select(country_id) - not used
def select_cities(country_id):
    sql = "SELECT * FROM cities WHERE country_id = %s"
    values = [country_id]
    results = run_sql(sql, values)
    cities = []
    for result in results:
        country = country_repository.select(result["country_id"])
        city = City(result["name"], country, result["id"])
        cities.append(city)
    return cities
     

#delete_all() - not used
def delete_all():
    sql="DELETE FROM cities"
    run_sql(sql)

#delete(id) - not used
def delete(id):
    sql = "DELETE FROM cities WHERE id=%s"
    values = id
    run_sql(sql, values)


# select_users(city_id) - not used
def select_users(city_id):
    users = []
    sql = "SELECT users.* FROM users INNER JOIN visits ON visits.user_id = users.id WHERE city_id = %s AND visits.visited = TRUE"
    values = [city_id]
    results = run_sql(sql, values)

    for result in results:
        user = User(result["name"], result["id"])
        users.append(user)
    return users

# select_visit by city_id - not used
def select_visits(city_id):
    visits=[]
    sql = "SELECT visits.* FROM visits INNER JOIN cities ON visits.city_id = cities.id WHERE city_id = %s AND visits.visited = TRUE"
    values = [city_id]
    results = run_sql(sql, values)
    for result in results:
        visit = Visit(result["user_id"], city_id, result["visited"], result["id"])
        visits.append(visit)
    return visits