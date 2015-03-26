hrs = raw_input("Enter Hours: ")
h = float(hrs)
rate = raw_input("Enter Rate: ")
r = float(rate)
if h >= 40:
    salary = (h-40) * r/2
    print salary + h * r
else:
    plus_hours = h-40
    plus_rate=1.5*rate
    salary_plus = ((h-plus_hours)*rate) + (plus_hours*plus_rate)
    print salary_plus
