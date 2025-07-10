from geometry import Square, Circle, area_stats

s = Square(3)
c = Circle(2)

print(s.area())
print(c.area())

shapes = [s, c]
print(area_stats(shapes))