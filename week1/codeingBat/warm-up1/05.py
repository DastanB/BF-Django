def parrot_trouble(talking, hour):
    if (talking == True) and (0 < hour < 7) or (talking == True) and (20 < hour < 24):
        return True
    else: return False