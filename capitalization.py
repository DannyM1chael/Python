def capitalization(investing, percent, duration):
    percent = int(percent)
    duration = int(duration)
    summa = 0
    summa = investing * pow((1 + percent/(12*100)), duration)
    return round(summa)

money = capitalization(10000, 10, 12)
print(money)