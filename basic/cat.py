from animal import Animal

class Cat(Animal) :
    def __init__(self) :
        super().setName("고양이")
        super().setSound("야옹")
        self.butler = True

