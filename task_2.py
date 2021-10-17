class Road:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_weight(self, spec_grav, thick):
        return self.length * self.width * spec_grav * thick / 1000

r = Road(5000, 20)
print(r.get_weight(25, 5))
