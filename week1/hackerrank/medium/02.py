import math

ab = int(input())
bc = int(input())
hypo = math.sqrt((ab*ab)+(bc*bc))
angle = math.degrees(math.acos(bc/hypo))
print(str(round(angle))+"°")