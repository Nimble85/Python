x = 4
y= 2
if not 1 + 1 == y or x == 4 and 7 == 8:
  print("Yes")
elif x > y:
  print("No")

print('\n','next_task', '\n')


i = 1
while i <=5:
   print(i)
   i = i + 1

print("Finished!")


print('\n','next_task', '\n')

i = 3
while i>=0:
   print(i)
   i = i - 1


print('\n','next_task', '\n')

x = 0
while x <= 20:
    print (x)
    x += 2


print('\n','next_task', '\n')

i = 5
while True:
    print (i)
    i = i -1
    if i <= 2:
        break


print('\n','next_task', '\n')

i = 0
while True:
   i = i +1
   if i == 2:
      print("Skipping 2")
      continue
   if i == 5:
      print("Breaking")
      break
   print(i)

print("Finished")

words = ["Hello", "world", "!"]
print(words[0])
print(words[1])
print(words[2])

print('\n','next_task', '\n','lists')

nums = [5, 4, 3, 2, 1]
print(nums[1])


print('\n','next_task', '\n')

empty_list = []
print(empty_list)

print('\n','next_task', '\n')


num = [5, 4, 3, [2], 1]
print(num[0])
print(num[3][0])
#print(num[5])

print('\n','next_task', '\n',end ='!!!!')
print("\n")
nums = [1, 2, 3, 4, 5]
nums[3] = nums[1]
print(nums[3])

print('\n','next_task', '\n', end='!!!')
print("\n")

nums = [10, 9, 8, 7, 6, 5]
nums[0] = nums[1] - 5
if 4 in nums:
  print(nums[3])
else:
  print(nums[4])




print('\n','next_task', '\n')
words = ["hello"]
words.append("world")    # функция добавляющая значение  в конец списка  (method)
print(words[1])

print('\n','next_task', '\n')
nums = [1, 3, 5, 2, 4]
print(len(nums))       # подсчёт кол-во элеменктов в списке (function)
print('\n','next_task', '\n')


words = ["Python", "fun"]
index = 1
words.insert(index, "is")    # insert a new item at any position in the list
print(words)

print('\n','next_task', '\n')

nums = [9, 8, 7, 6, 5]
nums.append(4)
nums.insert(2, 11)
print(len(nums))

print('\n','next_task', '\n')

letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))               # найти первое упоминание и вывести его индекс
print(letters.index('p'))
#print(letters.index('z'))


#
# max(list): Returns the list item with the maximum value
# min(list): Returns the list item with minimum value
# list.count(obj): Returns a count of how many times an item occurs in a list
# list.remove(obj): Removes an object from a list
# list.reverse(): Reverses objects in a list


print('\n','next_task', '\n')

numbers = list(range(10))   # возвращает последовательность чисел
print(numbers)

print('\n','next_task', '\n')

nums = list(range(5))
print(nums[4])

print('\n','next_task', '\n')


numbers = list(range(3, 8))
print(numbers)

print(range(20) == range(0, 20))

print('\n','next_task', '\n')


numbers = list(range(5, 20, 2))  # третий аргумент задаёт интервал
print(numbers)



print('\n','next_task', '\n')

nums = list(range(3, 15, 3))
print(nums[2])




print('\n','next_task', '\n')

words = ["hello", "world", "spam", "eggs"]
counter = 0
max_index = len(words) - 1

while counter <= max_index:
   word = words[counter]
   print(word + "!")
   counter = counter + 1



print('\n','next_task', '\n')

words = ["hello", "world", "spam", "eggs"]
for word in words:
  print(word + "!")


print('\n','next_task', '\n')

for i in range(5):
  print("hello!")

print('\n','next_task', '\n')

for i in range(0, 20, 2):
    print(i)


print('\n','next_task', '\n')
print('Final test')

list = [1, 1, 2, 3, 5, 8, 13]
print(list[list[4]])
print('List = ',list[list])

print('\n','next_task', '\n')
for i in range(10):
  if not i % 2 == 0:
    print(i+1)

print('\n','next_task', '\n')


print('\n','next_task', '\n')


print('\n','next_task', '\n')