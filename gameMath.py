import math


def GetAngle(p1, p2):
    return (p2[1] - p1[1]) / (p2[0] - p1[0])


def GetDistance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def GetPositionWithDistance(p1, p2, distance):  # y = a(x - p[0]) + p[1]
    if p1[0] == p2[0] and p1[1] == p2[1]:
        return (0, 0)
    minValueX = min(p1[0], p2[0])  # 2개의 점 중 x의 최솟값
    maxValueX = max(p1[0], p2[0])  # 2개의 점 중 x의 최댓값
    minValueY = min(p1[1], p2[1])  # 2개의 점 중 y의 최솟값
    maxValueY = max(p1[1], p2[1])  # 2개의 점 중 y의 최댓값
    x = (p2[0] * distance + p1[0] * (GetDistance(p1, p2) - distance)) / GetDistance(
        p1, p2
    )
    y = (p2[1] * distance + p1[1] * (GetDistance(p1, p2) - distance)) / GetDistance(
        p1, p2
    )
    print(x, y)
    return (x, y)


print(GetPositionWithDistance((0, 0), (5, 5), 1))
