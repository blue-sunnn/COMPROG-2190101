def distance1(x1, y1, x2, y2):
    # return the distance between points (x1, y1) and (x2, y2)
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def distance2(p1, p2):
    # p1 = [x1, y1] and p2 = [x2, y2]
    # return the distance between p1 and p1
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def distance3(c1, c2):
    # c1 = [x1, y1, r1] and c2 = [x2, y2, r2]
    # return the distance between the center of c1 and c2 
    # and display if c1 and c2 are overlapping or not
    d = distance2(c1[:2], c2[:2])
    if d <= (c1[2] + c2[2]):    ol = True
    else:                       ol = False
    return d, ol


def perimeter(points):
    # points = [[x1, y1], [x2, y2], ...]
    # use those points to calculate polygon perimeter
    d = []
    for i in range(len(points) - 1):
        d.append(distance2(points[i], points[i + 1]))
    d.append(distance2(points[len(points) - 1], points[0]))
    return sum(d)


exec(input().strip())
