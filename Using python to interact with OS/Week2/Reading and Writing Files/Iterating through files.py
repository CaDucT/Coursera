with open("spider.txt") as file:
    for line in file:
        print(line.upper().strip())

file = open("spider.txt")
lines = file.readlines()
file.close()
lines.sort()
print(lines)