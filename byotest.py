def number_of_evens(numbers):
    return 0


def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)


def test_not_equal(a, b):
    assert a != b, "Did not expect {0} but got {1}".format(a, b)


def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)

def test_not_in(collection, item):
    assert item not in collection, "{0} is in {1}".format(item, collection) 
    
def test_between(lower_limit , upper_limit, actual):
    assert lower_limit >= actual >= upper_limit, "{0} is not between {1} and {2}".format(actual, lower_limit, upper_limit)


# test_are_equal(7, 2)

# test_not_equal(5, 5)

# test_is_in([1,3,5,7,9, 10], 4)

# test_not_in([1,3,5], 3)

test_between(1, 50, 70)