def str_length(line):
    count = 0
    for i in line:
        count += 1
    return count
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert str_length("") == 0, "1st example";
    assert str_length("mo") == 2, "2st example";
    assert str_length("length") == 6, "3st example";

    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")



# def length(string):
#     count = 0
#     for i in string:
#         count += 1
#     return count