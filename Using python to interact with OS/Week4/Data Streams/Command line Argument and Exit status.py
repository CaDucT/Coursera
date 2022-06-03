import os.path
import sys

print(sys.argv)

#wc подсчет количества строк
# echo $? - статус чек 0 или 1

filename=sys.argv[1]

if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("New file created\n")

else:
    print("Error, the file {} already exists".format(filename))
    sys.exit(1)