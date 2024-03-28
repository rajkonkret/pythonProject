# iterator - klasa posiadajaca __iter__, __next__

class Count:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


counter = Count(1, 5)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

for i in Count(1, 5):
    print(i)

counter2 = Count(2, 10)
while True:
    try:
        number = next(counter2)
        print(number)
    except StopIteration:
        break
