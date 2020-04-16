
def foo(n):
    # Loop and print
    # foo(range(10)) = (0, 10) space complexity here is 1 aka only 1 thing prints
    for i in range(n):
        print(n)


'''
time complexity: O(n)
space complexity: O(1) (slots of memory)
'''


def bar(n):
    # Loop and print
    # foo(range(10)) = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] space complexity here is 10 because 10 things print
    for i in list(n):
        print(i)


'''
time complexity: O(n)
space complexity: O(n) (slots of memory)
'''


def foobar(n):
    print(n)
    if n > 0:
        foo(n-1)


'''
time complexity: O(n) (we are calling it n times so O of n)
space complexity: O(n) (all of the calls in the call stack take up a space in memory so O of n)
'''


def foo2(n):
    for i in range(n):
        print(i)
    # all arithmatic takes O(1) time...constant time..1*1 runs as fast as 100*100
    n = n * n
    return n


'''
time complexity:O(n)
space complexity:O(1)
'''


def foo3(n):
    for i in range(n):
        print(i)
    for k in range(n):
        print(i)
    for k in range(n):
        print(i)
    return n


'''
time complexity:O(3n) # not tested so it is O(3n), if nested it would be O(3)
space complexity:O(1)
'''


def foo4(n):
    for i in range(n):
        print(i)
        for k in range(n):
            print(i)
    for k in range(n):
        print(i)
    return n


'''
time complexity:O(n^2)
space complexity:O(1)
'''
