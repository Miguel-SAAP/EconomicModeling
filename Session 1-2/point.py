import random
from math import *


class Point:
    """
    Class modeling a real life 2D point
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """
        Magic method that defines how a point is printed
        Returns:
            string: A string representation of the point
        """
        return f"<{self.x}, {self.y}>"

    def __repr__(self):
        """
        Magic method that defines how a point is represented
        Returns:
            string: A string representation of the point
        """
        return self.__str__()

    def distance_orig(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __gt__(self, other):
        return self.distance_orig() > other.distance_orig()

    def __eq__(self, other):
        return self.distance_orig() == other.distance_orig()


if __name__ == "__main__":
    p1 = Point(1, 2)
    # p2 = Point(3, 4)
    # p3 = Point("James", "Jane")
    # print(p1.x, p1.y)
    # print(p1)

    points = []
    for i in range(5):
        # create a random point
        p = Point(random.randint(-100, 100), random.randint(-100, 100))
        points.append(p)

    print(points)
    p = Point(12, 5)
    print(p.distance_orig())

    p1 = Point(2, 4)
    p2 = Point(3, 3)

    points.sort()
    print(points)

    found = 0
    count = 0

    while found < 1000:
        count += 1
        p1 = Point(random.randint(-100, 100), random.randint(-100, 100))
        p2 = Point(random.randint(-100, 100), random.randint(-100, 100))
        if p1 == p2:
            found += 1
    print(found / found, count / found)