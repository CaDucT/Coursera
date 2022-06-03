import csv

with open("csv_file.txt") as file:
    csv_f = csv.reader(file)
    for row in csv_f:
        name,phone,role = row
        print(name,phone,role)
        print("Name: {}, Phone: {}, Role: {}".format(name,phone,role))
        print(row[0])