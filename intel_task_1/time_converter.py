import sys


def time_to_sec(s='1'):
    if not isinstance(s, str):
        raise TypeError('Wrong type of argument. Should be a string.')

    list_of_char_digits = list(map(str, range(10)))
    time_units = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400}

    for i in s[:-1]:
        if i not in list_of_char_digits + ['.']:
            raise TypeError('Wrong type of argument. Only digits are acceptable. '
                            'Acceptable time specifiers are \'s\', \'m\', \'h\', \'d\'')

    if s[-1] in list_of_char_digits + ['.']:
        return int(float(s))
    elif s[-1] in time_units.keys():
        return int(float(s[:-1]) * time_units.get(s[-1])) if len(s) > 1 else time_units.get(s[-1])
    else:
        raise TypeError('Wrong type of argument. Only digits are acceptable. '
                        'Acceptable time specifiers are \'s\', \'m\', \'h\', \'d\'')


if __name__ == "__main__":
    var = sys.argv[1]
    print(time_to_sec(var))
