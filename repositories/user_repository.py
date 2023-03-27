from db.run_sql import run_sql
from models.user import User
import pdb

# save(user)
def save(user):
    sql = "INSERT INTO users (name) VALUES (%s) RETURNING id"
    values = [user.name]
# Q what is this user here, from the User class?
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

# delete(id)

# update()

# select_locations_user_visited(user)