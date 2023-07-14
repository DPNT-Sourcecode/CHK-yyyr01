# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    if type(x) != int or type(y) != int:
        raise Exception("number should be a valid integer between 0 and 100")
    if (x > 100 or x < 0) or ( y > 100 or y < 0):
        raise Exception("number should be between 0 and 100")
    
    return x + y

print(compute(3,500))


