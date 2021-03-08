#Catherine Hu

def lpyear(year):
    if year % 4 != 0:
        return False

    if year % 100 != 0:
        return True

    if year % 400 == 0:
        return True
