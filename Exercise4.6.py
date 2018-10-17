def computepay(h,r):
        try:
            hrs = float(h)
            r = float(r)
            hrs >= 0
            r >= 0
        except:print('put in right number please')
        if hrs < 0:
            print('HOURES AND RATE MUST BIGGER THAN 0')
        elif r < 0:
            print('HOURES AND RATE MUST BIGGER THAN 0')
        elif hrs < 40:
            pay = hrs * r
        elif hrs >40:
            pay = 40 * r  + (hrs-40) * r * 1.5
        return pay
hrs = input("Enter Hours:")
p = computepay(hrs,10.5)
print("Pay",p)

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

xp = computepay(fh,hr)
print('Pay',xp)