import pdb

from models.user import User
import repositories.user_repository as user_repository

from models.country import Country
import repositories.country_repository as country_repository

from models.city import City
import repositories.city_repository as city_repository

from models.visit import Visit
import repositories.visit_repository as visit_repository

user_repository.delete_all()
country_repository.delete_all()
city_repository.delete_all()
visit_repository.delete_all()

user_1 = User("Wenjing")
user_repository.save(user_1)
user_2 = User("Dani")
user_repository.save(user_2)
user_3 = User("Javier")
user_repository.save(user_3)
user_4 = User("Tere Pepe")
user_repository.save(user_4)

country_1 = Country("Spain")
country_repository.save(country_1)
country_2 = Country("United Kingdom")
country_repository.save(country_2)
country_3 = Country("China")
country_repository.save(country_3)


city_1 = City("Sevilla", country_1)
city_repository.save(city_1)
city_2 = City("Madrid", country_1)
city_repository.save(city_2)
city_3 = City("Granada", country_1)
city_repository.save(city_3)
city_4 = City("Edinburgh", country_2)
city_repository.save(city_4)
city_5 = City("London", country_2)
city_repository.save(city_5)
city_6 = City("Manchester", country_2)
city_repository.save(city_6)
city_7 = City("Gaoan", country_3)
city_repository.save(city_7)
city_8 = City("Beijing", country_3)
city_repository.save(city_8)
city_9 = City("Shanghai", country_3)
city_repository.save(city_9)


visit_1 = Visit(user_1, city_1, True)
visit_repository.save(visit_1)
visit_2 = Visit(user_2, city_1)
visit_repository.save(visit_2)



# cities = user_repository.select_cities(user_2.id)
# for city in cities:
#     print(city.__dict__)

# cities = city_repository.select_cities(country_1.id)
# for city in cities:
#     print(city.name)

# users = city_repository.select_users(city_1.id)
# for user in users:
#     print(city_1.name +" is visited by " + user.name)

visits = visit_repository.select_all()
for visit in visits:
    print(visit.city.name + " - " + visit.user.name)
