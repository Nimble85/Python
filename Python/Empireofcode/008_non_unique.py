def non_unique(data):
    for i in data:
        if data.count(i) == 1:
            data.remove(i)



if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # Rank 1
    assert isinstance(non_unique([1]), list), "The result must be a list"
    assert non_unique([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert non_unique([1, 2, 3, 4, 5]) == [], "2nd example"
    assert non_unique([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    assert non_unique([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"

    # Rank 2
    assert non_unique(['P', 7, 'j', 'A', 'P', 'N', 'Z', 'i',
                       'A', 'X', 'j', 'L', 'y', 's', 'K', 'g',
                       'p', 'r', 7, 'b']) == ['P', 7, 'j', 'A', 'P', 'A', 'j', 'p', 7], "Letters"

    print("All done? Earn rewards by using the 'Check' button!")


# def checkio(text):
# 	text=text.lower(); l={}
# 	for i in text:
# 		if i.isalpha():
# 			if i in l.keys():
# 				l[i]=l.get(i)+1
# 			elif i not in l.keys():
# 				l[i]=1
# 	sort_key=l.keys(); sort_key.sort()
# 	if sum(l.values()) == len(l):
# 		return sort_key[0]
# 	else:
# 		index_v=l.values().index(max(l.values()))
# 		return l.keys()[index_v]
# 	#~ return sort_key, l.keys()
# 	#replace this for solution



#
# data = [1, 2, 3, 4, 5, 6]
# for i in data:
#      if data.count(i) == 1:
#            data.remove(i)
# print data
# Печатает [2,4,6]