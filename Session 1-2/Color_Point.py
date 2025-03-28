from point import Point
import random


class ColorPoint(Point):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return f"<{self.x}, {self.y}>, ({self.color})"


if __name__ == "__main__":
    color_points = []
    colors = ["red", "blue", "green", "yellow", "purple"]
    for i in range(5):
        p = ColorPoint(random.randint(-100, 100), random.randint(-100, 100), random.choice(colors))
        color_points.append(p)
    print("random color points: ")
    print(color_points)
    color_points.sort()
    print("color points sorted by distance: ")
    print(color_points)