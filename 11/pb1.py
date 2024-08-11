class TwoDworker:
    def __init__(self, i,j):
        self.i = i
        self.j = j
    def show_position(self):
        print(f"The position vectors for 2D are {self.i}i + {self.j}j")

class ThreeDworker(TwoDworker):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
    def show_position(self):
        print(f"The position vectos for 3D are {self.i}i + {self.j}j + {self.k}k")

c = TwoDworker(6, 4)
o = ThreeDworker(1, 2, 3)


c.show_position()

o.show_position()




