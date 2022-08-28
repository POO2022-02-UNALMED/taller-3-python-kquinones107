from televisores.tv import TV
from televisores.control import Control
from televisores.marca import Marca

if __name__ == "__main__":
    marca1 = Marca("Semsung")
    marca2 = Marca("Lj")

    tv1 = TV(marca1, True)
    tv2 = TV(marca2, False)

    tv1.setPrecio(2000)
    tv2.setCanal(90)
    tv1.setCanal(121)
    tv2.setVolumen(7)

    control1 = Control()
    control1.enlazar(tv1)
    control1.turnOff()
    control1.setCanal(50)
    control1.turnOn()
    control1.canalUp()
    control1.volumenUp()

    print(tv2.getCanal())
    print(tv1.getPrecio())
    print(tv1.getMarca().getNombre())
    print(tv1.getCanal())

class TV:

    numTV = 0

    def _init_(self, marca,  estado):

        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
        self._control = None
        self._class_.numTV += 1

    def setMarca(self, marca):
        self._marca = marca

    def getMarca(self):
        return self._marca

    def setControl(self, control):
        self._control = control

    def getControl(self):
        return self._control

    def setPrecio(self, precio):
        self._precio = precio

    def getPrecio(self):
        return self._precio

    def setVolumen(self, volumen):
        if volumen >= 0 and volumen <= 7 and self._estado:
            self._volumen = volumen

    def getVolumen(self):
        return self._volumen

    def setCanal(self, canal):
        if canal >= 1 and canal <= 120 and self._estado:
            self._canal = canal

    def getCanal(self):
        return self._canal

    @classmethod
    def setNumTV(cls, numTV):
        cls.numTV = numTV

    @classmethod
    def getNumTV(cls):
        return cls.numTV

    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._estado = False

    def getEstado(self):
        return self._estado

    def canalUp(self):
        if self._estado:
            if self._canal != 120:
                self._canal += 1
            else:
                self._canal = 1

    def canalDown(self):
        if self._estado:
            if self._canal != 1:
                self._canal -= 1
            else:
                self._canal = 120

    def volumenUp(self):
        if self._estado:
            if self._volumen < 7:
                self._volumen += 1

    def volumenDown(self):
        if self._estado:
            if self._volumen > 0:
                self._volumen -= 1

                
class Marca:

    def _init_(self, nombre):
        self._nombre = nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getNombre(self):
        return self._nombre

class Control:


    def _init_(self):
        self._tv = None

    def turnOn(self):
        self._tv.turnOn()

    def turnOff(self):
        self._tv.turnOff()

    def canalUp(self):
        self._tv.canalUp()

    def canalDown(self):
        self._tv.canalDown()

    def volumenUp(self):
        self._tv.volumenUp()

    def volumenDown(self):
        self._tv.volumenDown()

    def setCanal(self, canal):
        self._tv.setCanal(canal)

    def enlazar(self, tv):
        self._tv = tv
        self._tv.setControl(self)

    def setTv(self, tv):
        self._tv = tv

    def getTv(self):
        return self._tv