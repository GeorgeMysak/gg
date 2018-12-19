



def dataset(file_adress):
    file = open(file_adress, encoding='utf-8')
    data = {}
    lines = file.readlines()
   # print(lines)
    for line in lines[1:]:
        line=line.replace(' ','').strip('\n').split(',')
     #   print(line)
        if line[0] in data:
            if line[1] in data[line[0]]:
                data[line[0]][line[1]][line[2]] ={'quantity': line[3],
                                                'price':line[4]}
            else:
                dict[line[0]][line[1]] = {line[2]:
                                              {'quantity': line[3],
                                               'price': line[4]}}
        else:
            dict[line[0]] = {line[1]: {line[2]:
                                           {'quantity': line[3],
                                            'price': line[4]}}
                             }
    return data
    file.close()
print(dataset('orders.csv'))