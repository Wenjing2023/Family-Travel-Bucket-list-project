import pdb

from models.user import User
import repositories.user_repository as user_repository

from models.country import Country
import repositories.country_repository as country_repository

from models.city import City
import repositories.city_repository as city_repository

from models.visit import Visit
import repositories.visit_repository as visit_repository


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
city_2 = City("Edinburgh", country_2)
city_repository.save(city_2)
city_3 = City("Gaoan", country_3)
city_repository.save(city_3)

visit_1 = Visit(user_1, city_1, True)
visit_repository.save(visit_1)
visit_2 = Visit(user_2, city_2, True)
visit_repository.save(visit_1)
visit_3 = Visit(user_3, city_3, False)
visit_repository.save(visit_3)
visit_4 = Visit(user_4, city_3, False)
visit_repository.save(visit_4)

# pdb.set_trace()

print(visit_1.city.name +" is visited by " + visit_1.user.name)
print(visit_2.city.name +" is visited by " + visit_2.user.name)
