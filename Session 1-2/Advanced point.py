from colorpoint import ColorPoint


class AdvancedPoint(ColorPoint):  # Inherit from ColorPoint
    COLORS = ["red", "blue", "green", "black", "white"]

    def __init__(self, x, y, color):
        if not isinstance(x, (int, float)):
            raise TypeError("x must be a number")
        if not isinstance(y, (int, float)):
            raise TypeError("x must be a number")
        # super().__init__(x, y, color)
        if color not in self.COLORS:
            raise ValueError(f"color must be one of {self.COLORS}")
        self._x = x
        self._y = y
        self._color = color

        @classmethod
        def add_color(cls, new_color):
            cls.COLORS.append(new_color)

        @property
        def x(self):
            return self._x

        @property
        def y(self):
            return self._y

        @color.setter
        def color(self, new_color):
            if new_color not in self.COLORS:
                raise ValueError(f"color must be one of {self.COLORS}")
            self._color = new_color

        @staticmethod
        def distance_2_points(point1, point2):
            return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

        @staticmethod
        def from_dictionary(dict):
            x = dict.get("x", 10)
            y = dict.get("y", 20)
            color = dict.get("color", "black")
            return AdvancedPoint(x, y, color)


AdvancedPoint.add_color("amber")
p2 = AdvancedPoint(1, 2, "amber")
p1 = AdvancedPoint(3, 4, "red")
print(p2)