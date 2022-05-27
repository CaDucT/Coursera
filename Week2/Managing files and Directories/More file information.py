import os
import datetime
print(os.path.getsize("bsd.txt"))
print(os.path.getmtime("bsd.txt"))
timestamp = os.path.getmtime("bsd.txt")
print(datetime.datetime.fromtimestamp(timestamp))
print(os.path.abspath("bsd.txt"))