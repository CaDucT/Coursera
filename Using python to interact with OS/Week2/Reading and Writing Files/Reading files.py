file = open("spider.txt")
#file.write("HELLO WORLD")
print(file.read())
file.close()

with open("spider.txt") as file:
    print(file.readline())
