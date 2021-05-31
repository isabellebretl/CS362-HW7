def leapyear(x):
    if x % 4 == 0:
        if x % 100 == 0:
            return False
        return True