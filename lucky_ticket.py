def ticket_type(number):
    number = int(number)
    sum_left = 0
    sum_right = 0
    for i in range(6):
        if i < 3:
            sum_right += number // 10**i % 10
        else:
            sum_left += number // 10**i % 10
    if sum_left == sum_right:
        return('счастливый')
    elif abs(sum_left - sum_right) == 1:
        return("встречный")
    elif abs(sum_left - sum_right) == 2:
        return("пьяный")
    else:
        return("обычный")
        
result = ticket_type("123321")
print(result)