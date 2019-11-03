
def rect_intersect(x1, y1, w1, h1, x2, y2, w2, h2):
    x3 = x2
    y3 = y2
    x4 = x2 + w2
    y4 = y2 + h2
    x2 = x1 + w1
    y2 = y1 + h1

    x11 = max(min(x1, x2), min(x3, x4))
    x12 = min(max(x1, x2), max(x3, x4))
    y11 = max(min(y1, y2), min(y3, y4))
    y22 = min(max(y1, y2), max(y3, y4))

    if ((x12-x11) > 0) and ((y22 - y11) > 0):
        return (x12-x11)*(y22-y11)
    else:
        return 0

def rect_area(w, h):
    return w*h

def iuu(x1, y1, w1, h1, x2, y2, w2, h2):
    a1 = rect_area(w1, h1)
    a2 = rect_area(w2, h2)
    ai = rect_intersect(x1, y1, w1, h1, x2, y2, w2, h2)
    if ai == 0:
        return 0
    else:
        return ai/(a1+a2-ai)