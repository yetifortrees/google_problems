####
#This program is an optimized solution for determining how many points on a grid
#exist within a triangle. It uses picks theorem, which is:
#
#           A = i + b/2 - 1
#
#where A is the area of the triangle, b is the number of points on the boundary, and i
#is the number of internal points
####
import numpy
from fractions import gcd
def answer(vertices):
    x1 = vertices[0][0]
    x2 = vertices[1][0]
    x3 = vertices[2][0]
    y1 = vertices[0][1]
    y2 = vertices[1][1]
    y3 = vertices[2][1]
    originalVertices = list(vertices)
    for i in vertices:
        i.append(1)
    for i in vertices:
        i.append(i[0])
        i.append(i[1])
    Area = vertices[0][0]*vertices[1][1]*vertices[2][2]
    Area += vertices[0][1]*vertices[1][2]*vertices[2][3]
    Area += vertices[0][2]*vertices[1][3]*vertices[2][4]
    Area -= vertices[2][0]*vertices[1][1]*vertices[0][2]
    Area -= vertices[2][1]*vertices[1][2]*vertices[0][3]
    Area -= vertices[2][2]*vertices[1][3]*vertices[0][4]
    Area = abs(Area)/2
    pointsOn12 = gcd( abs(y2 - y1), abs(x2 - x1) )
    pointsOn23 = gcd( abs(y3 - y2), abs(x3 - x2) )
    pointsOn31 = gcd( abs(y1 - y3), abs(x1 - x3) )
    pointsOnEdge = pointsOn12 + pointsOn23 + pointsOn31
    #print(pointsOn12, pointsOn23, pointsOn31, pointsOnEdge)
    #Area = abs(numpy.linalg.det(vertices))/2
    return int(Area - (pointsOnEdge/2) + 1)

print(answer([[2, 3], [6, 9], [10, 160]]))
print(answer([[91207, 89566], [-88690, -83026], [67100, 47194]]))