import re

result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)
print(result.groups())
print(result[0])
print(result[1])
print(result[2])
print("{} {}".format(result[2], result[1]))

def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])

print(rearrange_name("Bektibay, Alina"))
print(rearrange_name("Turganbay, Nurlan"))
print(rearrange_name("Turganbay, Nurlan JR."))

def rearrange_name(name):
  result = re.search(r"^(\w*), (\w* Jr.)$", name)
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

name=rearrange_name("Nurlan, Turganbay Jr.")
print(name)