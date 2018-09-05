#golf=lambda s:(9<len(s))*(s.lower()>s>s.upper())*'?'>min(s)



#def golf(password):
#    golf = lambda s: (9 < len(s)) * (s.lower() > s > s.upper()) * '?' > min(s)
golf=lambda s:(min(s)<'A')*(s.lower()!=s!=s.upper())*(9<len(s))
 #   return True or False

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    golf('A1213pokl') == False
    golf('bAse730onE') == True
    golf('asasasasasasasaas') == False
    golf('QWERTYqwerty') == False
    golf('123456123456') == False
    golf('QwErTy911poqqqq') == True
    print("Use 'Check' to earn sweet rewards!")


#golf=lambda s:(min(s)<'A')*(s.lower()!=s!=s.upper())*(9<len(s))  it`s work too
