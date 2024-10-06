#!/usr/bin/python3
def pascal_triangle(n):
    """
    pascal triangle
    """
    triangle = []
    if n <= 0:
        return triangle
    triangle.append([1])
    for x in range(1, n):
        row = [1]
        prev_row = triangle[x-1]
        for j in range(1, len(prev_row)):
            row.append(prev_row[j-1] + prev_row[j])
        row.append(1)
        triangle.append(row)
    return triangle
