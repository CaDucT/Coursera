import os
def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename, "w") as file:
    a = file.write("pzdc")
    return filename

print(create_python_script("asd.py"))
