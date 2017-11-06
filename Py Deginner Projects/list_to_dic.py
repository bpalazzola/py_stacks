def make_dict(list1, list2):
    pairs = zip(list1, list2)
    new_dict = dict(pairs)
    return new_dict

# Test it out
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
print "Expected pairs: Anna & horse; Eli & cat; Pariece & spider; Brendan & giraffe; Amy & ticks; Shane & dolphins; Oscar & llamas"
print "Actual --------"
print make_dict(name, favorite_animal)