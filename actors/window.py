import os

class Window:
    def __init__(self, width: int, height: int) -> None:
        self.__width__ = width
        self.__height__ = height
        self.__oldWidth__ = os.get_terminal_size().columns
        self.__oldHeight__ = os.get_terminal_size().lines
        os.system(f'MODE {width},{height}')
        os.system('COLOR 0A')

    def __isValidFrame__(self, frame: list) -> bool:
        if len(frame) != self.__height__:
            return False
        for rowIndex in range(len(frame)):
            if len(frame[rowIndex]) != self.__width__:
                return False
        return True

    def dimensions(self) -> tuple:
        return (self.__width__,self.__height__)

    def load(self,frame: list,clean : bool = False) -> None:
        if not self.__isValidFrame__(frame):
            raise Exception("Invalid Frame Load")
        if(clean):
            os.system('CLS')
        for rowIndex in range(len(frame)):
            if len(frame) == rowIndex+1:
                print(frame[rowIndex],end='')
            else:
                print(frame[rowIndex])

    def destroy(self) -> None:
        os.system(f'MODE {self.__oldWidth__},{self.__oldHeight__}')
        os.system('COLOR 07')
