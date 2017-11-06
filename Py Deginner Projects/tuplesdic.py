def make_tuples(some_dict):
    return some_dict.items()


# Test it out
my_dict = {
    "Speros": "(555) 555-5555",
    "Michael": "(999) 999-9999",
    "Jay": "(777) 777-7777"
}
print 'Expected:[("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]'
print 'Actual -------'
print make_tuples(my_dict)
