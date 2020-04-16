'''
Cookies: 
You can eat either 1, 2, or 3 at a time...
how many combinations of 1, 2, or 3 at a time given n cookies

1
------
1


2
------
1, 1
2


3
------
1, 1, 1
2, 1
1, 2
3


4
------
1, 1, 1, 1
1, 2, 1
1, 1, 2
1, 3
2, 1, 1
2, 2
2, 1
3, 1

5
------
1, 1, 1, 1, 1
1, 1, 1, 2
1, 1, 2, 1
1, 2, 1, 1
2, 1, 1, 1
1, 1, 3
1, 3, 1
3, 1, 1
1, 2, 2
2, 2, 1
2, 1, 2
2, 3
3, 2

'''
# Possible Solutions:


def eating_cookies(n, cache=None):
    if cache is None:
        cache = [0] * (n + 1)
    if n <= 1:
        cache[n] = 1
        return 1
    if n == 2:
        cache[n] = 2
        return 2
    elif n in cache:
        return cache[n]
    else:
        cache[n] = eating_cookies(
            n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
        return cache[n]


def eating_cookies_2(n, cache=None):
    if cache is None:
        cache = [0] * (n + 1)
    if n <= 1:
        cache[n] = 1
    elif n == 2:
        cache[n] = 2
    elif cache[n] == 0:
        cache[n] = eating_cookies_2(
            n - 1, cache) + eating_cookies_2(n - 2, cache) + eating_cookies_2(n - 3, cache)
    return cache[n]
