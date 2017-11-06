class Underscore(object):

    def map(self):
         _.map()
    def reduce(self):
        _.reduce()
    def find(self):
        _.find()
    def filter(self):
        _.filter()
    def reject(self):
        _.reject()
# you just created a library with 5 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# should return [2, 4, 6] after you finish implementing the code above
