def capitalization(investing, percent, duration):
    percent = int(percent)
    duration = int(duration)
    for i in range(duration):
        investing += investing * percent/100 * duration/12
    return round(investing)

money = capitalization(10167, 10, 1)
print(money)