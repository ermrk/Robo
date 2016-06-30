from .Component import Component


class Fibonachi(Component):
    __i1 = 1
    __i2 = 1
    enabled = True

    def destroy(self):
        pass

    def update(self):
        if self.enabled:
            nextElem = self.__i1 + self.__i2
            self.__i1 = self.__i2
            self.__i2 = nextElem
            print(nextElem)

    def start(self):
        pass
