import pdb
from models.employee import Employee
import repositories.employee_repo as employee_repo

# employee_repo.delete_all()

employee1= Employee("Frank", "11/08/2021", "Bird Keeper", 5)
employee2= Employee("Morty","09/08/2021", "Apiary", 1, 10)
# employee_repo.add_employee(employee1)

# employee_repo.list_employees()

# employee_repo.find_employee(3)
employee_repo.update(employee2)
pdb.set_trace()