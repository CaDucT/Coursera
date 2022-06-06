import re
import operator
import csv

per_user = {}
error = {}



def open_files(file):
    with open(file, 'r') as f:
        for line in f:
            errorname = re.search(r'ERROR ([\w \']*)', line)
            if errorname != None:
                if errorname[1] not in error:
                    error[errorname[1]] = 1
                else:
                    error[errorname[1]] += 1
        sorted_errors = sorted(error.items(), key=operator.itemgetter(1), reverse=True)
        print(sorted_errors)

    with open('error_messages.csv', 'w', newline='') as csvfile:
        write = csv.writer(csvfile, delimiter=',')
        write.writerow(["Error", "Count"])
        for log in sorted_errors:
            key, value = log
            write = csv.writer(csvfile, delimiter=',')
            write.writerow([key, value])

    with open(file, 'r') as f:
        for line in f:
            usr_pat = re.search(r'\(([\w\.]*)\)', line)
            err_pat = re.search(r'(ERROR|INFO)', line)
            if usr_pat[1] not in per_user.keys():
                per_user[usr_pat[1]] = {}
                per_user[usr_pat[1]]['INFO'] = 0
                per_user[usr_pat[1]]['ERROR'] = 0

            if err_pat[1] == 'INFO':
                per_user[usr_pat[1]]['INFO'] += 1
            elif err_pat[1] == 'ERROR':
                per_user[usr_pat[1]]['ERROR'] += 1
        sorted_users = sorted(per_user.items())
        print(sorted_users)

    f = open('user_statistics.csv', 'w', newline='')
    write = csv.writer(f, delimiter=',')
    write.writerow(['Username', 'INFO', 'ERROR'])
    for stats in sorted_users:
        a, b = stats
        f.write(str(a) + ',' + str(b["INFO"]) + ',' + str(b["ERROR"]) + '\n')
    f.close()















open_files('syslog.log')


