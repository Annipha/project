with open('STATA.csv', mode='rU') as f:
    file_list = []
    for row in f:
        file_list.append(row)
print file_list[0]
