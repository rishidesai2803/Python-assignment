import math

print("Angle   Sin      Cos      Tan")
for a in range(0, 91, 15):
    rad = math.radians(a)
    s = math.sin(rad)
    c = math.cos(rad)
    t = math.tan(rad)
    print(a, "   ", round(s, 4), " ", round(c, 4), " ", round(t, 4))
