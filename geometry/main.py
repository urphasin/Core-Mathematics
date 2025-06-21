from shapely.geometry import Point, LineString, Polygon

# Creat a point
p = Point(2, 3)

# Create a line
line = LineString([(0, 0), (1, 1), (2, 2)])

# Create a polygon
triangle = Polygon([(0,0), (1, 0), (0.5, 1)])

# Area of polygon
print("Area:", triangle.area)

# Length of line
print("Length:", line.length)

# Distance between shapes
print("Distance between point and line:", p.distance(line))

# Check if point is inside the triangle
print("Point inside triangle?", triangle.contains(p))


square = Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])
circle = p.buffer(1)  # buffer creates a circular shape around a point

# Intersection
intersection = square.intersection(circle)

# Union
union = square.union(circle)

print("Intersection area:", intersection.area)


import matplotlib.pyplot as plt
from shapely.geometry import box
from shapely.plotting import plot_polygon, plot_line, plot_points

# For Shapely 2.0+, use plot methods
plot_polygon(square, facecolor="lightblue", edgecolor="black")
plot_polygon(circle, facecolor="red", edgecolor="black", alpha=0.5)
plt.axis("equal")
plt.show()
