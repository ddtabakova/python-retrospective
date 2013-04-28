from collections import OrderedDict


def groupby(func, seq):
    result = {}
    for x in seq:
        result.setdefault(func(x), []).append(x)
    return result


def compose(func1, func2):
    return lambda x: func1(func2(x))


def iterate(func):
    composed_func = lambda x: x
    while True:
        yield composed_func
        composed_func = compose(func, composed_func)


def zip_with(func, *iterables):
    return (func(*zipped) for zipped in zip(*iterables))


def cache(func, cache_size):
    if cache_size == 0:
        return func
    cache = OrderedDict()

    def func_cached(*args):
        if args not in cache:
            if cache_size == len(cache):
                cache.popitem(False)
            cache[args] = func(*args)

        return cache[args]

    return func_cached


def double(x):
        print('called "double"')
        return x * 2
