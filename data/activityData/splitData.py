# This python program takes data from the full *Activity files generated by the calculate.c program and calculates the coefficients for a double exponential function using that data. It will print the numbers to screen as well as appending the data to two files: alphaCoefficients and betaCoefficients.

import os, sys, inspect

# ensure pyeq2 can be imported
if os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..') not in sys.path:
    sys.path.append(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..'))
import pyeq2

if __name__ == "__main__":

	equation = pyeq2.Models_2D.Exponential.DoubleExponential()

# What this section does is reads the data from the file given and formats it so the zunzun.com code can read it. We need two separate Strings so we can have two equations found.
	alpha = 'X\tY\n'
	beta = 'X\tY\n'
	f = open(sys.argv[1],'r')
	while f:
		line = f.readline()
		if len(line) != 0:
			if line[0] != '#':
# Instead of doing character by character as in the C code of calculate.c, this next line simply splits the numbers according to a delimiter and assigns the data* variables those numbers.
				data1,data2,data3,data4 = line.split(',')
# Append the data to the alpha and beta variables (will be used for the y values later)
				alpha = alpha + data1 + "\t" + data2 + "\n"
				beta = beta + data3 + "\t" + data4 + "\n"
		else:
			break

	fileName = sys.argv[1]

#fit plot to alpha data 
#This is where the magic happens for fitting the data. As you can see, it uses many calls from the zunzun code while printing and storing the data. I mostly reused an example code from the zunzun source to do this part.
	data = alpha
	pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(data, equation, False)
	equation.Solve()
    
	print("This is for alpha data:\n")
	print equation.GetDisplayName(), str(equation.GetDimensionality()) + "D"
	print equation.fittingTargetDictionary[equation.fittingTarget], '=', equation.CalculateAllDataFittingTarget(equation.solvedCoefficients)
	print "Fitted Parameters:"
#So we have the coefficients solved. I basically told it to print each value and then append the data to the file.
# NOTE TO SELF: At first glance, it looks like I may be calculating the coefficients twice for each function (1 to print, 1 print to file) If that's the case, I need to assign those to variables to save comp time
	for i in range(len(equation.solvedCoefficients)):
		print "    %s = %-.16E" % (equation.GetCoefficientDesignators()[i], equation.solvedCoefficients[i])

	alphaFile = open("alphaCoefficients","a")
	alphaFile.write(fileName[0:8] + "," +  str(equation.CalculateAllDataFittingTarget(equation.solvedCoefficients))+",")
	for i in range(len(equation.solvedCoefficients)):
		alphaFile.write(str(equation.solvedCoefficients[i])+",")
	alphaFile.write('\n')

#fit plot to beta data
	data = beta
	pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(data, equation, False)
	equation.Solve()
    
	print("\nThis is for beta data:\n")
	print equation.GetDisplayName(), str(equation.GetDimensionality()) + "D"
	print equation.fittingTargetDictionary[equation.fittingTarget], '=', equation.CalculateAllDataFittingTarget(equation.solvedCoefficients)
	print "Fitted Parameters:"
	for i in range(len(equation.solvedCoefficients)):
		print "    %s = %-.16E" % (equation.GetCoefficientDesignators()[i], equation.solvedCoefficients[i])

	betaFile = open("betaCoefficients","a")
	betaFile.write(fileName[0:8] + "," + str(equation.CalculateAllDataFittingTarget(equation.solvedCoefficients))+",")
	for i in range(len(equation.solvedCoefficients)):
		betaFile.write(str(equation.solvedCoefficients[i])+",")
	betaFile.write('\n')

	alphaFile.close()
	betaFile.close()
	f.close()
