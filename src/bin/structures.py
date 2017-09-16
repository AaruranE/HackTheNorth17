
class Zone:

    def __init__(self, x, y, radius):
        if x is None or y is None or radius is None:
            raise ValueError("All zone parameters must be numeric")
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        self.x = x
        self.y = y
        self.radius = radius

    def contains(self, other_zone):
        distance_squared = (self.x - other_zone.x)**2 + (self.y - other_zone.y)**2
        return distance_squared <= self.radius **2