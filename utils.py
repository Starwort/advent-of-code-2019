import typing


def permutations_of(
    *args: typing.Any,
) -> typing.Generator[typing.Tuple[typing.Any, ...], None, None]:
    values = set(args)
    for i in values:
        remaining = values - {i}
        if remaining:
            for objects in permutations_of(*remaining):
                yield (i, *objects)
        else:
            yield i,


def deep_loop(
    *args: typing.Iterable,
) -> typing.Generator[typing.Tuple[typing.Any, ...], None, None]:
    for i in args[0]:
        if args[1:]:
            for objects in deep_loop(*args[1:]):
                yield (i, *objects)
        else:
            yield i,


def float_range(
    start: float, stop: float = None, step: float = 1, /
) -> typing.Generator[float, None, None]:
    if stop is None:
        stop = start
        start = 0
    if step == 0:
        raise ValueError("step cannot be negative")
    if step < 0:
        while start > stop:
            yield start
            start += step
    else:
        while start < stop:
            yield start
            start += step
