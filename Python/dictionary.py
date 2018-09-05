d = {}
d = {'dict': 1, 'dictionary': 2}

print(d)

# second way create dictionary

d = dict(short='dict',long='dictionary')

d = dict([(1, 1), (2, 4)])


# third way create dictionary
d = dict.fromkeys(['a', 'b'])

d = dict.fromkeys(['a', 'b'], 100)


# four way to create dictionary

d = {a: a ** 2 for a in range(7)}
