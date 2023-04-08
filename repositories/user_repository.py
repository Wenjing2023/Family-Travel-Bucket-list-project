from db.run_sql import run_sql
from models.city import City
from models.user import User
import repositories.country_repository as counrty_repository
import pdb

# save(user)
def save(user):
    sql = "INSERT INTO users (name) VALUES (%s) RETURNING id"
    values = [user.name]
    results = run_sql(sql, values)
    user.id = results[0]['id']

# select_all()
def select_all():
    sql = "SELECT * FROM users"
    results = run_sql(sql)
    users = []
    for result in results:
        user = User(result["name"], result["id"])
        users.append(user)
    return users

# select(id)
def select(id):
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    user = None
    results = run_sql(sql, values)
    if results:
        user = User(results[0]["name"], results[0]["id"])
    return user

# delete_all()
def delete_all():
    sql="DELETE FROM users"
    run_sql(sql)

# delete(id)
def delete(id):
    sql = "DELETE FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# update(user)
def update(user):
    sql = "UPDATE users SET name = %s WHERE id = %s"
    values = [user.name, user.id]
    run_sql(sql,values)


# select_cities_by(user) - not used
def select_cities(user_id):
    sql = "SELECT cities.* FROM cities INNER JOIN visits ON visits.city_id = cities.id WHERE user_id =%s AND visits.visited = TRUE"
    values = [user_id]
    cities = []
    results = run_sql(sql, values)
    for result in results:
        country_id = result["country_id"]
        country = counrty_repository.select(country_id)
        city = City(result["name"], country, result["id"])
        cities.append(city)
    return cities
 

