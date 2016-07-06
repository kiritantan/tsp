import enum


class MstName(enum.Enum):

    def __new__(cls):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    BaseMst = ()
    Prim = ()
    Kruskal = ()
