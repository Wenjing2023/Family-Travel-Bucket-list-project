from db.run_sql import run_sql
from models.country import Country


# save(country)
def save(country):
    sql = "INSERT INTO countries (name) VALUES (%s) RETURNING id"
    values = [country.name]
    results = run_sql(sql, values)
    country.id = results[0]['id']

# select_all()
def select_all():
    countries = []
    sql = "SELECT * FROM countries"
    results = run_sql(sql)
    for result in results:
        country = Country(result["name"], result["id"])
        countries.append(country)
    return countries
    
# select(id)
def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        country = Country(results[0]["name"], results[0]["id"])
    return country
# delete_all()
# delete(id)
# update(country)
