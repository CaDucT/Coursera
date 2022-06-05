#!/usr/bin/env python3

import re
import os

error = {}
per_user = {}

with open('syslog.log', 'r') as f:
    for line in f:
        username = re.search(r'\(([\w.]*)\)', line)
        if username[1] not in per_user:
            per_user[username[1]] =0
        per_user[username[1]] += 1
        """else:
            errorname = re.search(r'ERROR ([\w ]*)', line)
            if errorname[1] not in error:
                error[errorname[1]] = 0
            error[errorname[1]] += 1"""


    print(per_user)
    print(error)




#Jan 31 00:09:39 ubuntu.local ticky: INFO Created ticket [#4217] (mdouglas)