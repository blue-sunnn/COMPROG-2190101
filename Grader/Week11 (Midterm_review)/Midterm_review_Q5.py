# function1
def create_record():
    # get input from keyboard: messy travel records
    # return: records - a list of lists of records
    temp = []
    while True:
        x = input()
        if x == 'q': break
        temp.append(x.split())
    return temp


# function2
def sort_list(records):
    # input: a list of lists of record
    # return: sorted_records - sorted version of the input
    temp = []
    for i in records:
        d, m, y = [int(e) for e in i[1].split('/')]
        temp.append([i[0], y, m, d, i[2]])
    return [[j[0], str(j[3]) + '/' + str(j[2]) + '/' + str(j[1]), j[4]] for j in sorted(temp)]


# function3
def create_output(sorted_records):
    # input: sorted records
    # return: (1) a list of user’s name and (2) a list of trip’s details with the
    # index of each list corresponding to one another
    names, trips = [], []
    for rec in sorted_records:
        name = rec[0]
        trip = rec[1] + ':' + rec[2]
        if name not in names:
            names.append(name)
            trips.append([trip])
        elif name in names:
            trips[names.index(name)] += [trip]
    return names, trips


# the main function
def main():
    # call these three methods
    # print out the sorted output in the correct format back to the user
    x = create_record()
    if len(x) == 0:
        print('No records!')
    else:
        y = sort_list(x)
        names, trips = create_output(y)
        for i in range(len(names)): print(names[i], trips[i])


exec(input())
