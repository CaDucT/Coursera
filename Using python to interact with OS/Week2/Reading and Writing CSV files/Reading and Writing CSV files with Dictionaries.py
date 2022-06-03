import csv

with open("software.csv") as software:
    reader = csv.DictReader(software)
    for row in reader:
        print(("{} has {} users".format(row["name"], row["users"])))

users = [{"name": "Nurlan", "username": "CaDucT", "department": "IT analyst"},
         {"name": "Alina", "username": "Guacamolle", "department": "LPA"}]

keys = ["name", "username", "department"]
with open('by_department.csv', "w") as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)
