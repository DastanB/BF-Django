def squirrel_play(temp, is_summer):
    if is_summer:
        return 60 <= temp <= 100
    else:
        return 60 <= temp <= 90
