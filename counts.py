def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])
        
#   or...............
#
#   count = 0
#    for c in message:
#        if c.isupper():
#            count += 1
#    return count
        
print(count_upper_case("How Many Capitals ARE there IN this"))
assert count_upper_case("") == 0, "Empty string"
assert count_upper_case("A") == 1, "One upper case"
assert count_upper_case("AA") == 2, "Two upper case"
assert count_upper_case("aa") == 0, "Two lower case"
assert count_upper_case("a") == 0, "One lower case"
assert count_upper_case("$%%^") == 0, "Special characters"
assert count_upper_case("1345") == 0, "Numbers"
assert count_upper_case("aaS45%^&DFG") == 4, "Four upper case in a mix"

print("All the tests passed")