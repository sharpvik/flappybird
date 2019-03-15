#
# Created by Viktor A. Rozenko Voitenko
#

# To use this test() function you need to pass it:
# 1. expected value precisely
# 2. name of the function you wish to test (callable object) 
#    without brackets
# 3. list of arguments if needed
#
# If the function in question does not expect any arguments you can
# simply explude the last arguments to the test() function -- 
# just pass the first two (expect and func).
#
# The call to test() can look something like this:
# test(5, add, [3, 2])
def test(expect, func, args=None):
    if args == None:
        return func() == expect
    return func(*args) == expect



# test_multiple() function accepts a list of calls to 
# the test() function and returns the percentage of successfully
# passed tests.
#
# The call to test_multiple() can look something like this:
# tests = [
#   test(5, add, [3, 2]),
#   test('Hannah', name),
#   test('Hello, James!', greet, ['James'])
# ]
# test_multiple(tests)
def test_multiple(tests):
    return sum(tests) / float( len(tests) ) * 100
