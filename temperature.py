cels =  raw_input('Enter the Celsius:')
celsius = float(cels)
farent = raw_input('enter the fahrenheit')
far = float(farent)
f= celsius*9/5+32
c=(f-32)*5/9
# print fahrenheit
print ('%0.1f degree Celsius is equal to %0.1f degree fahrenheit' %(celsius, f))
# print the celsius 
print c 
