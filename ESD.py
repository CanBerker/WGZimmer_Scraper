row_data = list()

row_data.append(1)
row_data.append("a\n\n")

for item in row_data :
    item.replace('\n', ' ').replace('\r', '')
print row_data