import re

print(re.split(r"[.?!]", "One sentence. Two sentence? Three sentence!"))
print(re.split(r"([.?!])", "One sentence. Two sentence? Three sentence!"))

print(re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com"))
print(re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada"))