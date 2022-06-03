from resource import *
import time
import psutil

time.sleep(1)
print(getrusage(RUSAGE_SELF))

for i in range(10**8):
    _ = 1+1

print(psutil.cpu_percent(0.5))
print(getrusage(RUSAGE_SELF))