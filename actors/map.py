from actors.window import Window


class Map:
    def __init__(self, window: Window, mapFile: str = '') -> None:
        self.__window__ = window
        self.__map__ = {}
        self.__frame__ = []
        if mapFile == '':
            self.__empty__()
        else:
            self.__read__(mapFile)
        self.__render__()
        self.__window__.load(self.__frame__)

    def __empty__(self) -> None:
        dim = self.__window__.dimensions()
        width = dict()
        for i in range(dim[0]):
            width.clear()
            for j in range(dim[1]):
                width[j] = 0
            self.__map__[i] = width

    def __read__(self, mapFileName: str) -> None:
        with open(f'./maps/{mapFileName}.map') as mapFile:
            mapData = mapFile.readlines()
            for row in range(len(mapData)):
                if len(mapData)-1 != row:
                    mapData[row] = mapData[row][:-1]
                else:
                    mapData[row] = mapData[row]
            if not self.__isValidMapData__(mapData):
                raise ValueError(
                    f"Can not read a valid map from the map file {mapFile}")

    def __isValidMapData__(self, mapData: list) -> bool:
        loadableMapData = {}
        loadableRow = {}
        dim = self.__window__.dimensions()
        if len(mapData) != dim[1]:
            return False
        for rowIndex in range(len(mapData)):
            if len(mapData[rowIndex]) != dim[0]:
                f = len(mapData[rowIndex])
                return False
            loadableRow = {}
            for elementIndex in range(len(mapData[rowIndex])):
                if mapData[rowIndex][elementIndex] not in ['0', '1']:
                    return False
                else:
                    loadableRow[elementIndex] = mapData[rowIndex][elementIndex]
            loadableMapData[rowIndex] = loadableRow
        self.__map__ = loadableMapData
        return True

    def __render__(self) -> list:
        decoder = self.__loadDecoderSymbols__()
        for mapRow in range(len(self.__map__)):
            row = ''
            for elementIndex in range(len(self.__map__[mapRow])):
                elementHash = self.__getElementHash__((mapRow, elementIndex))
                row = row + decoder[elementHash]
            self.__frame__.append(row)

    def __getElementHash__(self, elementIndex: tuple) -> str:
        elementHash = ''
        dim = self.__window__.dimensions()
        for row in range(elementIndex[0]-1, elementIndex[0]+2):
            for col in range(elementIndex[1]-1, elementIndex[1]+2):
                if col < 0 or row < 0 or col+1 > dim[0] or row+1 > dim[1]:
                    element = 0
                else:
                    element = self.__map__[row][col]
                elementHash = elementHash + str(element)
        return elementHash

    def __loadDecoderSymbols__(self) -> dict:
        decoder = {}
        with open('./maps/dec.sym', encoding='utf-8') as symbols:
            readSymbols = symbols.readlines()
            for symbol in readSymbols:
                encoding, char = symbol.split('|', 1)
                decoder[encoding] = char[:1]
        return decoder
