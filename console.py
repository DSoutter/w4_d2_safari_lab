import pdb
from models.employee import Employee
from models.animal import Animal
import repositories.employee_repo as employee_repo
import repositories.animal_repo as animals_repo

# employee_repo.delete_all()

employee1= Employee("Frank", "11/08/2021", "Bird Keeper", 5)
employee2= Employee("Morty","09/08/2021", "Apiary", 1, 10)
# employee_repo.add_employee(employee1)

animal1 = Animal("Sergei", "Bear")
animals_repo.add_animal(animal1)
# employee_repo.list_employees()

# employee_repo.find_employee(3)
employee_repo.update(employee2)
pdb.set_trace()