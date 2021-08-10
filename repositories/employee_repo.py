from pdb import run
from db.run_sql import run_sql

from models.employee import Employee
import repositories.employee_repo as employee_repo

# Add a delete all method
def delete_all():
    sql= "DELETE FROM employees"
    run_sql(sql)

# Add a member of staff
def add_employee(employee):
    sql = "INSERT INTO employees (name, start_date, department, performance) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [employee.name, employee.start_date, employee.department, employee.performance]
    results = run_sql(sql, values)
    id = results[0]['id']
    employee.id = id
    return employee

# List all employees
def list_employees():
    employees = []
    
    sql = "SELECT * FROM employees"
    results = run_sql(sql)

    for row in results:
        employee = Employee(row['name'], row['start_date'], row['department'], row['performance'])
        employees.append(employee)
    return employees

# Find a specific member of employees
def find_employee(id):
    employee = None
    sql = "SELECT * FROM employees WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        employee = Employee(result['name'], result['start_date'], result['department'], result['performance'])
    return employee

# Remove a member of staff
def delete(id):
    sql="DELETE FROM employees WHERE id = %s"
    values= [id]
    run_sql(sql, values)
    

# Update a member of staff
def update(employee):
    sql = "UPDATE employees SET (name, start_date, department, performance) = (%s, %s, %s, %s) WHERE id = %s"
    values = [employee.name, employee.start_date, employee.department, employee.performance, employee.id]
    run_sql(sql, values)
    

