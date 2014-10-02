numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

numbers.extend([1,2,3])

strings.append("hello")
strings.append("world")

# write your code here
second_name = names[1]


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

print names

sortednames = sorted(names)

print sortednames
#names.sort()
# #return names
# sortednames = names
# print sortednames