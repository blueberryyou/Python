class Circle:
    _radius=0.0
    def  __init__(self,a):
        self._radius=a
    def get_perimeter(self):
        print(round(2*3.14*self._radius,2))
    def get_area(self):
        print(round(3.14*self._radius*self._radius,2))
o=Circle(3)
o.get_perimeter()
o.get_area()

