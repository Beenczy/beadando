def Exercise11():
    for i in range(100,1000):
        for j in range(100,1000):
            x=i*j
            if str(x) == str(x)[::-1]:
                y = str(x)
                a = i
                b = j
    return '{0} * {1} = {2}'.format(a, b, y)

print(Exercise11())
