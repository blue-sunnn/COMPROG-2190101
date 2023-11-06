def remove_patterns(strings):  # Task 4.1
    # strings is in the format:
    # original_string,pattern_1,pattern_2,….
    # Find ALL patterns within the original_string and remove them out. If
    # the same pattern found more than once, remove all of them.
    # All remaining fragmented substrings need to be concatenated together
    # in order and return as a new string called edited_string (See
    # Figure 4.1 to see how this function works)
    # Write your code here
    x = strings.split(',')
    original, patterns = x[0], x[1:]

    for pattern in patterns:
        while pattern in original:
            i = original.find(pattern)
            original = original[:i] + original[i + len(pattern):]

    return original


def coverage(s, p):
    out = []
    k = s.find(p)
    while k >= 0:
        out += [[k, k + len(p)]]
        k = s.find(p, k+len(p))
    return out


def check_coverage(strings):  # Task 4.2
    # strings is in the format:
    # reference_string,pattern_1,pattern_2, ….
    # Check if patterns when aligned to the reference string will cover all
    # characters within the reference string.
    # Return string “Covered” if they can cover, otherwise return the
    # indices of all positions in the references that are not covered
    # (See Figure 4.2 to see how this function works
    # Hint: You can use find()
    x = strings.split(',')
    original, patterns = x[0], x[1:]
    covers = []
    
    for pattern in patterns:
        cov = coverage(original, pattern)
        if cov:
            covers += cov
    covers.sort()

    notcovered = []
    first, last = 0, len(original)

    for cov in covers:
        if cov[0] > first:
            notcovered += [[first, cov[0] - 1]]
        first = cov[1]
    if cov[1] < last:
        notcovered += [[cov[1], last - 1]]
    if notcovered:
        out = ''
        for e in notcovered:
            out += str(e[0])+'-'+str(e[1])+','
        out = out[:-1]
    else:
        out = 'Covered'

    return out


# Do not remove the following statement
exec(input().strip())
