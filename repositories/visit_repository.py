from db.run_sql import run_sql
from models.visit import Visit
import repositories.user_repository as user_repository
import repositories.city_repository as city_repository

# save(visit)
def save(visit):
    sql = "INSERT INTO visits (user_id, city_id, visited) VALUES (%s, %s, %s) RETURNING *"
    values = [visit.user.id, visit.city.id, visit.visited]
    results = run_sql(sql, values)
    visit.id = results[0]["id"]
    return visit

# select_all()
def select_all():
    sql = "SELECT * FROM visits"
    results = run_sql(sql)
    visits = []
    for result in results:
        user = user_repository.select(result["user_id"])
        city = city_repository.select(result["city_id"])
        visit = Visit(user, city, result["visited"], result["id"])
        visits.append(visit)
    return visits

# select(id) 
def select_visit(visit_id):
    visit = None
    sql = "SELECT * FROM visits WHERE id = %s"
    values = [visit_id]
    results = run_sql(sql, values)
    if results:
        user = user_repository.select(results[0]["user_id"])
        city = city_repository.select(results[0]["city_id"])
        visit = Visit(user, city,results[0]["visited"],visit_id)
    return visit
        

# delete_all()
def delete_all():
    sql="DELETE FROM visits"
    run_sql(sql)

# delete (id)
def delete(id):
    sql = "DELETE FROM visits WHERE id=%s"
    values = [id]
    run_sql(sql, values)

# update (visit)
def update(visit):
    sql = "UPDATE visits SET (user_id, city_id, visited) = (%s, %s, %s) WHERE id=%s"
    values = [visit.user.id, visit.city.id, visit.visited, visit.id]
    run_sql(sql, values)


