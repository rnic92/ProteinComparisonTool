def substr_after(s, delim):
    return s.partition(delim)[2]


def substr_before(s, delim):
    return s.partition(delim)[0]
