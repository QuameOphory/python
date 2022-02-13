def customized_range(*args):
    start, step = 0, 1
    numargs = len(args)
    if numargs < 1:
        raise TypeError(f'expected at least one argument. got {numargs}')
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        start, stop = args
    elif numargs == 3:
        start, stop, step = args
    else:
        raise TypeError(f'Expected at most three arguments. Got {numargs}')

    while start <= stop:
        yield start
        start += step

for i in customized_range(25, 100, 5):
    print(i, end=' ')