for num in range(1, 1000) if range % !=0
    print(range)


a = [1, 2, 5, 10, 255, 3]
sum = 0
for val in a:
    sum = sum+val
print(sum)

a = [1, 2, 5, 10, 255, 3]
sum = 0
for val in a:
    sum = sum+val
avg = sum/len(a)
print (avg)

lower = int(input(0))
upper = int(input(1000))
for i in range(lower, upper + 1):
    if(i % 2 != 0):
        print(i)
#multiples A
for count in range(1, 1001, 2):
    print count
#multiples B
for count in range(5, 1000001, 5):
    print count
#sum list
my_numbers = [1, 2, 5, 10, 255, 3]
sum = 0
for i in my_numbers:
    sum += i
print sum
#average list
print sum / len(my_numbers)
