inp = raw_input('Enter Fahrenheit Temperature:')
 Try:
	fahr = float(inp)
	 cel=(fahr-32.0)*5.0/9.0
	 print cel
except:
	print 'Please enter a number'

