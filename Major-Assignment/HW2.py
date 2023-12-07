# HW2 Football-League-Table (*** DO NOT DELETE this line or add line before this ***)
# Only add your code in the provided area.
# DO NOT delete or modified the given code in main()

def toString(table):
    # create a string that represents the table for printing
    # for example if the table is: [["Arsenal",0,0,0,0,0],["Chelsea",0,0,0,0,0],["Liverpool",0,0,0,0,0]]
    # this method will return a string that can be printed as a table

    # Team        |Pld|Pts|Dif|For|Agst|
    # Arsenal     |  0|  0|  0|  0|   0|
    # Chelsea     |  0|  0|  0|  0|   0|
    # Liverpool   |  0|  0|  0|  0|   0|

    # team name can have up to 12 characters
    # Pld, Pts, Dif, For can have up to 3 characters
    # Agst can have up to 4 characters

    # enter your code here
    temp = ["Team        |Pld|Pts|Dif|For|Agst|"]
    for team in table:
        Team = (str(team[0]) + ' ' * (12 - len(team[0])))
        Pld = (' ' * (3 - len(str(team[1])))) + str(team[1])
        Pts = (' ' * (3 - len(str(team[2])))) + str(team[2])
        Dif = (' ' * (3 - len(str(team[3])))) + str(team[3])
        For = (' ' * (3 - len(str(team[4])))) + str(team[4])
        Agst = (' ' * (4 - len(str(team[5])))) + str(team[5])
        t = Team + '|' + Pld + '|' + Pts + '|' + Dif + '|' + For + '|' + Agst + '|'
        temp.append(t)

    table = '\n'.join(temp)
    return table + '\n'

def createTable(s):
    # create table from team names, for example: "Arsenal Liverpool Chelsea"
    # return the created table, for example: [["Arsenal",0,0,0,0,0],["Chelsea",0,0,0,0,0],["Liverpool",0,0,0,0,0]]
    # the created table must be sorted according to function "sortTable"

    # enter your code here
    temp = [[i, 0, 0, 0, 0, 0] for i in s.split()]
    return sortTable(temp)

def sortTable(table):
    # sort table by the following fields in order:
    # Pts (descending)
    # Dif (descending)
    # For (descending)
    # Agst (ascending)
    # teamname (ascending)
    # Pld (ascending)
    # return the sorted table

    # enter your code here
    temp = sorted([[-k[2], -k[3], -k[4], k[5], k[0], k[1]] for k in table])
    return [[k[4], k[5], -k[0], -k[1], -k[2], k[3]] for k in temp]

def saveTable(table):
    # save the table to file "table.txt" (as a ready-to-print string)
    # also print the table out

    # enter your code here
    s_table = toString(table)
    f = open('table.txt', 'w')
    f.write(s_table)
    f.close()
    print(s_table)

def match(table, team1, team2, score1, score2):
    # input is the table, team1 name, team2 name, goals that team1 scores, goals that team2 scores
    # if team1 and team2 are the same, just report and return table
    # if either team is not in the table, report accordingly and return table
    # otherwise, update the table and return the updated table that is already sorted

    # enter your code here
    teamname = []
    for i in table:
        teamname.append(i[0])
        if i[0] == team1: team1 = i
        if i[0] == team2: team2 = i

    if team1[0] == team2[0]: print("Error: a team plays the same team!")
    elif team1[0] not in teamname and team2[0] not in teamname: print("Error: Both team do not exist in the table!")
    elif team1[0] not in teamname: print("Error: First team does not exist in the table!")
    elif team2[0] not in teamname: print("Error: Second team does not exist in the table!")
    else:
        table.pop(table.index(team1))
        table.pop(table.index(team2))
        # pts
        if score1 == score2:
            team1[2] += 1
            team2[2] += 1
        elif score1 > score2:
            team1[2] += 3
        elif score1 < score2:
            team2[2] += 3
        # pld
        team1[1] += 1
        team2[1] += 1
        # dif
        team1[3] += (score1 - score2)
        team2[3] += (score2 - score1)
        # for
        team1[4] += score1
        team2[4] += score2
        # agst
        team1[5] += score2
        team2[5] += score1

        table = table + [team1] + [team2]

    return sortTable(table)

def changePoint(table, team, point):
    # change the Pts of the given team by "point" amount (can be positive and negative integer)
    # return the updated table after point change (the table must be sorted again)

    # enter your code here
    teamname = []
    for i in table:
        teamname.append(i[0])
        if i[0] == team: team = i
    if team[0] in teamname:
        table.pop(table.index(team))
        team[2] += point
        table.append(team)

    return sortTable(table)

def removeTeams(table, toRemove):
    # remove some team from the table ,
    # toRemove is a list of team names to remove, for example: ["Southampton", "Arsenal", "Liverpool"]
    # return the updated table (must already be sorted again)

    # enter your code here
    temp = [i for i in table if i[0] not in toRemove]
    return sortTable(temp)

def addTeams(table, toAdd):
    # add some team to the table,
    # toAdd is a list of team names to add, for example: ["Southampton", "Arsenal", "Liverpool"]
    # set all numbers associated with the newly added teams to 0
    # return the updated table (must already be sorted again)
    # Assume that the name of team will never duplicate with existing ones in the table!

    # enter your code here
    temp = [[i, 0, 0, 0, 0, 0] for i in toAdd]
    return sortTable(table + temp)

def resetTable(table):
    # reset all number information in the table to 0
    # return the updated table (already sorted again)

    # enter your code here
    temp = [[i[0], 0, 0, 0, 0, 0] for i in table]
    return sortTable(temp)

def loadFile(filename):
    # make a table from a given text file
    # the text file form is similar to the following example (actual file is also given)
    # Be careful, there are white spaces to make the table readable:

    # Team        |Pld|Pts|Dif|For|Agst|
    # Blackburn   |  2|  3|  1|  3|   2|
    # Southampton |  1|  3|  1|  2|   1|
    # Chelsea     |  2|  3| -1|  3|   4|
    # Arsenal     |  1|  1|  0|  4|   4|
    # Liverpool   |  1|  1|  0|  4|   4|
    # Everton     |  1|  0| -1|  1|   2|

    # return the table (must be sorted)

    # enter your code here
    table = []
    f = open(filename, 'r')
    temp = f.readlines()
    f.close
    for i in temp[1:]:
        t = i.split()
        t = ''.join(t)
        table.append(t[:-1].split('|'))

    for i in table:
      for j in range(1, 6):
        i[j] = int(i[j])

    return sortTable(table)