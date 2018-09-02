def alarm_clock(day, vacation):
    if vacation:
        if 0 < day <= 5: return "10:00"
        else: return 'off'
    else: 
        if 0 < day <= 5: return "7:00"
        else: return '10:00'