from db.run_sql import run_sql

from models.employee import Employee
# import repositories.user_repository as user_repository

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

# List all staff


# Find a specific member of staff


# Remove a member of staff


# Update a member of staff

