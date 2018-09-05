def sure_not(line):
    if 'not ' not in line:
        return 'not ' + line
    elif 'not' in line:
        return line
    else:
        return 'not ' + line

#    return line

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sure_not("sure") == "not sure", "1st example";
    assert sure_not("not sure") == "not sure", "2st example";
    assert sure_not("noter") == "not noter", "3st example";

    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")








# Given a string, return a new string where "not " has been added to the front.
# However, if the string already begins with "not", return the string unchanged.

# С учетом строки верните новую строку, в которой «нет» было добавлено в начало.
# Однако, если строка уже начинается с «not», верните строку без изменений.
#

######SUCESS!!!!#####


def sure_not(line):
    if 'not ' not in line:
        return 'not ' + line
    elif 'not ' in line:
        return line
    else:
        return 'not ' + line


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sure_not("sure") == "not sure", "1st example";
    assert sure_not("not sure") == "not sure", "2st example";
    assert sure_not("noter") == "not noter", "3st example";

    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")
