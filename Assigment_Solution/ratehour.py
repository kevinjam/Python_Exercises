hours = raw_input('Enter Hour: ')
hr = float(hours)
rates = raw_input('Enter rate: ')
rat = float(rates)
if hr >= 40:
     gross_pay = (hr-40) * rat/2

print gross_pay + hr *rat
