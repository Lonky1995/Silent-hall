def comutepay(hours,rate):
    print('In computepay,hours,rate')
    if hours > 40:
        reg = rate * hours
        otp = (hours - 40) * (rate * 0.5)
        pay = reg + otp
    else:
        pay = hours * rate
    print('Returning',pay)
    return pay

sh = input("Enter Hours:")
sr = input("Enter Ratel")
fh = float(sh)
fr = float(sr)
pay = comutepay(fh,fr)
print('Pay',pay)