def computepay(h,r):
    if h >= 40:
        m = (h-40) * r/2
    return m + h * r
    return 

hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Enter Rate:")
r = float(rate)
print computepay(h,r)
