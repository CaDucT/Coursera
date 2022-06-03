import re

print(re.search(r".com", "welcome"))
print(re.search(r"\.com", "welcome"))
print(re.search(r"\.com", "google.com"))

print(re.search(r"\w*", "This is an example"))
print(re.search(r"\w*", "This_is_another_example"))
print(re.search(r"[\w ]*", "This is an example"))
print(re.search(r"[\w\s\d\.@#$%^&*!]*", "This sen has 2 words and _!@#$%^&* symbols"))