from pdb import run
from db.run_sql import run_sql

from models.employee import Employee
from models.animal import Animal

import repositories.animal_repo as animals_repo

# Add a delete all method
def delete_all():
    sql= "DELETE FROM animals"
    run_sql(sql)

# Add a member of staff
def add_animal(animal):
    sql = "INSERT INTO animals (name, type) VALUES (%s, %s) RETURNING *"
    values = [animal.name, animal.type]
    results = run_sql(sql, values)
    id = results[0]['id']
    animal.id = id
    return animal

# List all animals
def list_animals():
    animals = []
    
    sql = "SELECT * FROM animals"
    results = run_sql(sql)

    for row in results:
        animal = Animal(row['name'], row['type'])
        animals.append(animal)
    return animals

# Find a specific animal of animals
def find_animal(id):
    animal = None
    sql = "SELECT * FROM animals WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        animal = Animal(result['name'], result['type'])
    return animal

