words = "It's thanksgiving day. It's my birthday,too!"

x = [2,54,-2,7,12,98]
print max(x)

x = ["hello",2,54,-2,7,12,98,"world"]
print min(x)
print max(x)

x = [19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]
x = [-3, -2, 2, 6, 7, 10, 12, 19, 32, 54, 98]
print (x)
#find and replace
string = "If monkeys like bananas, then I must be a monkey!"
print string
print string.find("monkey")
string = string.replace("monkey", "alligator")
print stringwords = "It's thanksgiving day. It's my birthday,too!"

x = [2,54,-2,7,12,98]
print max(x)

x = ["hello",2,54,-2,7,12,98,"world"]
print min(x)
print max(x)

x = [19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]
x = [-3, -2, 2, 6, 7, 10, 12, 19, 32, 54, 98]
print (x)
#find and replace
string = "If monkeys like bananas, then I must be a monkey!"
print string
print string.find("monkey")
string = string.replace("monkey", "alligator")
print string

#min and max
x = [2, 54, -2, 7, 12, 98]
print x
print min(x)
print max(x)

#first and last
x = ["hello", 2, 54, -2, 7, 12, 98, "world"]
print x[0], x[len(x) - 1]

#new list
x = [19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]
print x
x.sort()
print x
# optional first parameter of slice defaults to zero
first_list = x[:len(x) / 2]
# optional second parameter of slice defaults to the list's length
second_list = x[len(x) / 2:]
print "first list", first_list
print "second_list", second_list
second_list.insert(0, first_list)
print second_list
