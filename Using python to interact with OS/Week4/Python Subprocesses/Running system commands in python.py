import subprocess
print(subprocess.run(["date"]))
print(subprocess.run(["sleep", "1"]))
result = subprocess.run(["ls", "this_file_does_not_exist"])
print(result.returncode)