import os
os.system('cls')


print("Generador de ID para empleados de Paolettos")
name = input("Write your name: ") 
last_name = input("Write your last name: ")
year_birth = input("Now the year you were born: ")

employee_id = f"{last_name.upper()}_{year_birth}"
print(f"Access granted to {name} {last_name}. Your user ID is: {employee_id}") #Generated standard ID format: lastname_yearbirth
