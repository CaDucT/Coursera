#!/usr/bin/env python3

import re
import operator
import csv

error = {}
per_user = {}
user_count = []

def open_files(file):
    with open(file, 'r') as f:
        data = f.readlines()
        return data

def generate_dict(data):
    for line in data:
        username = re.search(r'\(([\w\. ]*)\)', line)
        errorname = re.search(r'ticky: ERROR ([\w ]*)', line)

        if errorname != None:
            if errorname[1] not in error:
                error[errorname[1]] = 1
            else:
                error[errorname[1]] += 1
        elif username != None:
            if username[1] not in per_user:
                per_user[username[1]] = {}
                per_user[username[1]]['INFO'] = 0
                per_user[username[1]]['ERROR'] = 0
                if errorname != None:
                    per_user[username[1]]['ERROR'] = 1
                else:
                    per_user[username[1]]['INFO'] = 1
            else:
                if errorname != None:
                    per_user[username[1]]['ERROR'] += 1
                else:
                    per_user[username[1]]['INFO'] += 1
    errors_list = sorted(error.items(), key=operator.itemgetter(1), reverse=True)
    errors_list.insert(0, ('Error', 'Count'))
    per_user_list = sorted(per_user.items(), key=operator.itemgetter(0))
    per_user_list.insert(0, ('Username', {'INFO', 'ERROR'}))

    with open('error_messages.csv', 'w') as f:
        writer = csv.writer(f)
        for key, value in errors_list:
            writer.writerow([key, vale])

    with open('user_statistics.csv', 'w') as f2:
        writer = csv.writer(f2)
        for i, key in per_user_list:
            if i != 'Username':
                for j, x in key.items():
                    if len(user_count) == 2:
                        user_count.clear()
                    user_count.append(x)
                writer.writerow([i, user_count[0], user_count[1]])

print(open_files('syslog.log'))








#Jan 31 00:09:39 ubuntu.local ticky: INFO Created ticket [#4217] (mdouglas)