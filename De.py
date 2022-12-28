import random
class De:
    face=0
    def __self__(self):
        self.face=0
    def __str__(self):
        return f"De {self.face}"

    def lancer(self):
        self.face=random.randint(1,6)
        if self.face==6:
            self.face="Asticot"


