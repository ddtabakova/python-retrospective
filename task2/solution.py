def groupby(f, seq):
    return {f(x): [i for i in seq if f(i) == f(x)] for x in seq}

def zip_with(f, *iterables):
    if iterables == ():
        return []
    min_len = min([len(it) for it in iterables])
    print(min_len)
    for i in range(min_len):
        yield f(*[it[i] for it in iterables])
