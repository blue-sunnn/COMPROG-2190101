import string

def no_lowercase(t):
    for i in t:
        if i in string.ascii_lowercase:
            return False
    return True


def no_uppercase(t):
    for i in t:
        if i in string.ascii_uppercase:
            return False
    return True


def no_number(t):
    for i in t:
        if i in string.digits:
            return False
    return True


def no_symbol(t):
    for i in t:
        if i in string.punctuation:
            return False
    return True


def character_repetition(t):
    for i in range(len(t) - 3):
        if t[i] == t[i + 1] == t[i + 2] == t[i + 3]:
            return True
    return False


def number_sequence(t):
    num = '01234567890'
    for i in range(len(t) - 3):
        if t[i:i + 4] in num or t[i:i + 4] in num[::-1]:
            return True
    return False


def letter_sequence(t):
    t = t.lower()
    lower = string.ascii_lowercase
    for i in range(len(t) - 3):
        if t[i:i + 4] in lower or t[i:i + 4] in lower[::-1]:
            return True
    return False


def keyboard_pattern(t):
    t = t.lower()
    r0, r1, r2, r3 = '!@#$%^&*()_+', 'qwertyuiop', 'asdfghjkl', 'zxcvbnm'
    for i in range(len(t) - 3):
        if t[i:i + 4] in r0 or t[i:i + 4] in r0[::-1]: return True
        if t[i:i + 4] in r1 or t[i:i + 4] in r1[::-1]: return True
        if t[i:i + 4] in r2 or t[i:i + 4] in r2[::-1]: return True
        if t[i:i + 4] in r3 or t[i:i + 4] in r3[::-1]: return True
    return False


passw = input().strip()
error = []

if len(passw) < 8:              error.append('Less than 8 characters')
if no_lowercase(passw):         error.append('No lowercase letters')
if no_uppercase(passw):         error.append('No uppercase letters')
if no_number(passw):            error.append('No numbers')
if no_symbol(passw):            error.append('No symbols')
if character_repetition(passw): error.append('Character repetition')
if number_sequence(passw):      error.append('Number sequence')
if letter_sequence(passw):      error.append('Letter sequence')
if keyboard_pattern(passw):     error.append('Keyboard pattern')
if len(error) == 0:             error.append('OK')

for i in error: print(i)
