# text = 'Hello world 123'
#
# print(text)
# #print(len(text))
# text = text.lower()
# l = {}
#
# for i in text:
#     if i.isalpha():
#         print(i)
#         if i.
# # def checkio(text):
# #     text=text.lower()
# #     l = {}
# #     for i in text:
# #         if i.isalpfa():
# #             if i in l.keys():
# #                 l[i] = l.get(i) + 1
# #             elif



def checkio(text):
	text=text.lower(); l={}
	for i in text:
		if i.isalpha():
			if i in l.keys():
				l[i]=l.get(i)+1
			elif i not in l.keys():
				l[i]=1
	sort_key=l.keys(); sort_key.sort()
	if sum(l.values()) == len(l):
		return sort_key[0]
	else:
		index_v=l.values().index(max(l.values()))
		return l.keys()[index_v]
	#~ return sort_key, l.keys()
	#replace this for solution


	#These "asserts" using only for self-checking and not necessary for auto-testing
print  checkio(u"Hello World!") == "l", "Hello test"
print  checkio(u"How do you do?") == "o", "O is most wanted"
print  checkio(u"One") == "e", "All letter only once."
print  checkio(u"Oops!") == "o", "Don't forget about lower case."
print  checkio(u"AAaooo!!!!") == "a", "Only letters."
print  checkio(u"abe") == "a", "The First."
print  checkio(u"fsbd") == "b"
	#~ print("Start the long test")
print  checkio(u"a" * 9000 + u"b" * 1000) == "a", "Long."
	#~ print("The local tests are done.")
''' "fsbd" '''

