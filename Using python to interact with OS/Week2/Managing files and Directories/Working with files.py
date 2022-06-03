import os
#os.remove("novel.txt")
with open("asd.txt", "w") as f:
    f.write("New text")
#os.rename("asd.txt", "bsd.txt")
print(os.path.exists("asd.txt"))
print(os.path.exists("ssd"))
