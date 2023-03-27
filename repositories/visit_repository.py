from db.run_sql import run_sql
from models.visit import Visit
import repositories.user_repository as user_repository
import repositories.city_repository as city_repository

# save(visit)
def save(visit):
    sql = "INSERT INTO visits (user_id, city_id, visited) VALUES (%s, %s, %s) RETURNING id"
    values = [visit.user.id, visit.city.id, visit.visited]
    results = run_sql(sql, values)
    visit.id = results[0]["id"]

# select_all()
def select_all():
    sql = "SELECT * FROM visits"
    results = run_sql(sql)
    visits = []
    for result in results:
        user = user_repository.select(result("user_id"))
        city = city_repository.select(result("city_id"))
        visit = Visit(user, city, result["visited"], result["id"])
        visits.append(visit)
    return visits

# select_location(visit_id)
# select_user(city_id)
# user(visit)
# delete_all()
# delete(id)
# update(visit)
