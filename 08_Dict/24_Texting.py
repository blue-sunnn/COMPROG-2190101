import string

def reverse(d):
    temp = {d[k]: k for k in d}
    return temp


k2t = {
    '0': ' ',
    '2': 'a', '22': 'b', '222': 'c',
    '3': 'd', '33': 'e', '333': 'f',
    '4': 'g', '44': 'h', '444': 'i',
    '5': 'j', '55': 'k', '555': 'l',
    '6': 'm', '66': 'n', '666': 'o',
    '7': 'p', '77': 'q', '777': 'r', '7777': 's',
    '8': 't', '88': 'u', '888': 'v',
    '9': 'w', '99': 'x', '999': 'y', '9999': 'z'
}

t2k = reverse(k2t)


def text2keys(text):
    s = []
    for i in list(text.lower()):
        if i in string.ascii_lowercase or i == ' ':
            s.append(t2k[i])
    return ' '.join(s)


def keys2text(keys):
    s = ''
    for i in keys.split():
        s += k2t[i]
    return s


exec(input().strip())  # must have this line when submitting to grader
