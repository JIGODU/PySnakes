from actors.map import Map


class Snake:
    def __init__(self, map: Map) -> None:
        self.__length__ = 3
        self.__head__ = ()
        self.__trail__ = []
        self.__spawn__(map)

    def __spawn__(self, map: Map) -> None:
        pass

    def __len__(self) -> int:
        return self.__length__
