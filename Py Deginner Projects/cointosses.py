import random

def cointoss():
    print "flip"
    for i in range(5000):
        if i %2 == 0:
            print "flip is"+ str(i)
            print "Its heads"
        else:
            print "flip is"+ str(i)
            print "Its tails"
cointoss()

total_heads = 0
total_tails = 0
count = 0


while count < 5000:

    coin = random.randint(1, 2)
