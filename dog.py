from animal import Animal

class Dog(Animal) :
    def __init__(self) :
        super().setName("강아지")
        super().setSound("멍멍")
        self.master = True
    