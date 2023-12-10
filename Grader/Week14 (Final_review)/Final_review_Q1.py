def get_consensus(ss):
    # write your code here.
    consensus = get_consensus_generic(ss)
    return consensus  # DO NOT MODIFY THIS LINE


def get_consensus_generic(ss):
    # write your code here.
    ii = ss.upper().split('\n')
    longest = max([len(i) for i in ii])
    char = sorted(list(set(''.join(ii))))
    counting_dict = {k: [0] * longest for k in char}

    for s in ii:
        for e, c in enumerate(s):
            counting_dict[c][e] += 1

    data = []
    for k in char:
        data.append(counting_dict[k])

    max_each_col = []
    max_symbol = [[] for _ in range(longest)]
    for j in range(longest):
        col_data = [data[i][j] for i in range(len(data))]
        max_each_col.append(max(col_data))
        for i in range(len(char)):
            if data[i][j] == max_each_col[j]:
                max_symbol[j].append(char[i])

    consensus = ' '.join(['/'.join(i) for i in max_symbol])
    return consensus  # DO NOT MODIFY THIS LINE


exec(input().strip())
