def count_down_from(min):
    count = min
    while count > 0:
        yield count
        count -= 1


def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1


c_u = count_up_to(3)
c_d = count_down_from(3)


def combine(gen1, gen2):
    yield from gen1
    yield from gen2


com = combine(c_u, c_d)
print(next(com))
print(next(com))
print(next(com))
print(next(com))
print(next(com))
print(next(com))
