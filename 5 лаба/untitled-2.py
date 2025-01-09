class circus:
    def __init__(self, radius):
        self.r = radius
    def get_radius(self):
        return "Радиус шара: {}".format(self.r)    
    def set_radius(self, new_radius):
        self.r = new_radius
        return "новый радиус {}".format(new_radius)
x = circus(35)
print(x.get_radius())
print(x.set_radius(50))
