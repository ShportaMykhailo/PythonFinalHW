import re
from enum import unique

from utils.filesystem import read_file

filename = "Data.txt"

data = read_file(filename)
lines = re.split(" |, |\n", data)
data = data.splitlines()
# print(lines)
username = 1
ip = 8
time_list = [lines[5], lines[5]]
time = 5
connection_duration = 10
time_spent = dict()
users = dict()
unique_ip = dict()
unique_ip_count = dict()
seconds = 0
for idx in data:
    seconds = seconds + int(lines[connection_duration][5:7]) + int(lines[connection_duration][2:4]) * 60 + int(lines[connection_duration][0]) * 3600
    if lines[username] not in users:
        users[lines[username]] = 1
        unique_ip[lines[username]] = list()
        unique_ip[lines[username]].append(lines[ip])
        unique_ip_count[lines[username]] = 1
        time_spent[lines[username]] = seconds
    else:
        users[lines[username]] = users[lines[username]] + 1
        if lines[ip] not in unique_ip[lines[username]]:
            unique_ip[lines[username]].append(lines[ip])
            unique_ip_count[lines[username]] = unique_ip_count[lines[username]] + 1
            time_spent[lines[username]] = time_spent[lines[username]] + seconds
    if lines[time][6:10] > time_list[1][6:10]:
        time_list[1] = lines[time]
    elif lines[time][6:10] == time_list[1][6:10]:
        if lines[time][3:5] > time_list[1][3:5]:
            time_list[1] = lines[time]
        elif lines[time][3:5] == time_list[1][3:5]:
            if lines[time][0:2] > time_list[1][0:2]:
                time_list[1] = lines[time]
            elif lines[time][0:2] < time_list[0][0:2]:
                time_list[0] = lines[time]
        elif lines[time][3:5] < time_list[0][3:5]:
            time_list[0] = lines[time]
    elif lines[time][6:10] < time_list[0][6:10]:
        time_list[0] = lines[time]
    username = username + 11
    ip = ip + 11
    time = time + 11
    connection_duration = connection_duration + 11
unique_users = len(users)
