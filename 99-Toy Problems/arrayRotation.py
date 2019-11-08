def rotLeft(a, d):
    for i in range(d):
        a.append(a.pop(0))
    return a