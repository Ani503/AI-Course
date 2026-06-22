# Rectangle
length = 5
width = 3
rect_area = length * width
rect_perimeter = 2 * (length + width)
print(f"Rectangle: Area = {rect_area}, Perimeter = {rect_perimeter}")

# Triangle (using base and height for area, and all sides for perimeter)
base = 4
height = 6
side1 = 4
side2 = 5
side3 = 6
tri_area = 0.5 * base * height
tri_perimeter = side1 + side2 + side3
print(f"Triangle: Area = {tri_area}, Perimeter = {tri_perimeter}")

# Circle
radius = 7
circle_area = math.pi * radius ** 2
circle_perimeter = 2 * math.pi * radius
print(f"Circle: Area = {circle_area:.2f}, Perimeter (Circumference) = {circle_perimeter:.2f}")

# Rhombus (using diagonals d1 and d2 for area, and side for perimeter)
d1 = 8
d2 = 6
side = 5
rhombus_area = (d1 * d2) / 2
rhombus_perimeter = 4 * side
print(f"Rhombus: Area = {rhombus_area}, Perimeter = {rhombus_perimeter}")