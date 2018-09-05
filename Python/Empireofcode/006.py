def convert(str_number, radix):
    return -1


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert convert("AF", 16) == 175, "Hex"
    assert convert("101", 2) == 5, "Bin"
    assert convert("101", 5) == 26, "5 base"
    assert convert("Z", 36) == 35, "Z base"
    assert convert("AB", 10) == -1, "B > A > 10"

    print("Use 'Check' to earn sweet rewards!")

######IN_WORK!!!!#####
  # Иногда роботы смешивают свои координаты и используют другие системы Numeral.Попробуем разобраться
  # в этом и посмотреть, что может произойти.Вам предоставляется положительное число в виде cтроки вместе с
  # основанием для нее.Ваша функция должна преобразовать ее в десятичную форму.Радиус меньше 37 и больше 1.
  # Задача использует цифры и буквы A - Z  для строк.Следите за случаями, когда число не может быть преобразовано.Например: «1
  # A» не может быть преобразовано с помощью  radix 9.  Для этих случаев ваша функция должна возвращать - 1.
  #
  #

#
# Sometimes the robots mix up their coordinates and use other Numeral systems.
# Let's try to sort this out and see what could be going on.
# You are given a positive number as a string along with the radix for it. Your function should convert it into decimal form.
# The radix is less than 37 and greater than 1. The task uses digits and the letters A-Z for the strings.
# Watch out for cases when the number cannot be converted. For example: "1A" cannot be converted with radix 9.
# For these cases your function should return -1.