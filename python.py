# this programm is to calculate a userinput
num = raw_input('Enter your hour:')
# allowing the user to enter integers
hours = int(num)
num2 = raw_input('Enter Rate:')
# accepting the rate as float numbers only 
rate = float(num2)
pay = hours * rate
print pay
