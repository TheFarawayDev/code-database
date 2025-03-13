import math

def distance(first_point, second_point):
    x1 = first_point[0]
    y1 = first_point[1]
    x2 = second_point[0]
    y2 = second_point[1]

    x_diff_squared = pow(x2 - x1, 2)
    y_diff_squared = pow(y2 - y1, 2)

    total_squared = x_diff_squared + y_diff_squared
    result = math.sqrt(total_squared)

    return result

point1 = (1, 2)
point2 = (4, 6)
print(distance(point1, point2))