from typing import Optional


class Sample:
    def __init__(self,
                 a: int,
                 b: int,
                 c: int,
                 d: int,
                 e: Optional[str] = None) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e

    # __repr__
    def __repr__(self):
        e_repr = "tekst dla none" if self.e is None else self.e
        return (f"a={self.a},"
                f"b={self.b},"
                f"c={self.c},"
                f"d={self.d},"
                f"e={e_repr}")


ob = Sample(1, 2, 3, 4, 5)
print(ob)
ob2 = Sample(1, 2, 3, 4, "A")
ob3 = Sample(1, 2, 3, 4)
print(ob2)
print(ob3)  # a=1,b=2,c=3,d=4,e=None
