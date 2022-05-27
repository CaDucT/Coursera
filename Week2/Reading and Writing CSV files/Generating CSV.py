import csv

hosts = [["workstation.local", "192.168.1.1"], ["webserver.cloud", "10.2.5.6"]]
with open('hosts.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(hosts)