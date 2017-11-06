import random

def grades():
    print "score"
    for i in range(10):
        print "make a grade"
        grade = random.randint(0,100)
        print grade
        if grade <60:
            print "score is: " +str(grade)+"Your grade is F"
        elif grade >60 and grade <70:
            print "score is: " +str(grade)+"Your grade is D"
        elif grade > 70 and grade < 80:
            print "score is: " + str(grade) + "Your grade is C"
        elif grade > 80 and grade < 90:
            print "score is: " + str(grade) + "Your grade is B"
        elif grade > 90 and grade < 100:
            print "score is: " + str(grade) + "Your grade is A"
grades()
