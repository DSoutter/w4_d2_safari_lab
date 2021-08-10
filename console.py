import pdb
from models.employee import Employee
import repositories.employee_repo as employee_repo

employee_repo.delete_all()

employee1= Employee("Jerry", "10/08/2021", "Zoo Keeper", 2)

employee_repo.add_employee(employee1)
