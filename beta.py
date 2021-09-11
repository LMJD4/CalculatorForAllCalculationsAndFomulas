#first Python Calculator that uses Python 3

from decimal import *
from fractions import Fraction
import math

alphaOrderArr = []
vari = 1
varia = 2


#start loop
while vari < 10:

	#functions
	def lcm(k,l):
		return k*l/(math.gcd(k,l))

	def sqrt(numberToBeRooted):
		return numberToBeRooted**0.5
	
	def fractioner(numerator, denominator):
		theGCD = math.gcd(numerator, denominator)
		finalNumerator = numerator/theGCD
		finalDenominator = denominator/theGCD
		if finalDenominator == 1:
			return int(finalNumerator)
		if finalDenominator != 1:
			return str(int(finalNumerator)) + "/" + str(int(finalDenominator))
			
	def findFactors(number):
		factors = []
		output = ""
		for i in range(1, number):
			if number%i == 0:
				if i not in factors:
					dividend = int(number/i)
					output = output + str(i) + " , " + str(dividend) + "\n"
					factors.append(i)
					factors.append(dividend)
		return output
		
	def reduceRoots(root):
		factors = []
		radArg = 0
		rootExp = 0
		for i in range(2, root):
			if root%i == 0:
				if i not in factors:
					dividend = int(root/i)
					factors.append(i)
					factors.append(dividend)
		for i in factors:
			sqrtd = math.sqrt(i)
			rndsqrtd = math.ceil(sqrtd)
			if sqrtd-rndsqrtd == 0:
				radArg = int(root/i)
				rootExp = int(sqrtd)
				break;
		if radArg == 0 and rootExp == 0:
			output = "sqrt " + str(root)
		else:
			output = str(rootExp) + " root " + str(radArg)
		return output
				




	equation = input("What would you like to do? (Type man or manual for a list of operators): ")
	
	equation = equation.lower()
	
	
	
	if equation == "man" or equation == "manual":
	
		print("")
		print("Manual Shortcuts")
		print("Add Fractions")
		print("Addition")
		print("Alphabetical Order")
		print("distance")
		print("Divide Fractions")
		print("Division")
		print("Find Factors")
		print("Greatest Common Divisor")
		print("Lowest Common Multiple")
		print("Midpoint")
		print("Multiplication")
		print("Multiply Fractions")
		print("Power")
		print("Prime numbers")
		print("Quadratic Formula")
		print("Slope")
		print("Square Root")
		print("Subtract Fractions")
		print("Subtraction")
		print("")


	if equation == "manual shortcuts" or equation == "mshort":
		
		print("")
		print ("All Manual Shorcuts Or Short Forms:")
		print("")
		print("Manual Shortcuts: \"MShort\"")
		print("Add Fractions: \"fracadd\"")
		print("Addition: \"add\", \"+\"")
		print("Alphabetical Order: \"alphaorder\"")
		print("Distance: \"length\"")
		print("Divide Fractions: \"divfrac\"")
		print("Division: \"divide\", \"/\"")
		print("Find Factors: \"factors\"")
		print("Greatest Common Divisor: \"gcd\"")
		print("Lowest Common Multiple: \"lcm\"")
		print("Midpoint: \"mid\"")
		print("Multiplication: \"multiply\", \"times\", \"*\"")
		print("Multiply Fractions: \"multfrac\"")
		print("Power: \"to the power of\"")
		print("Prime numbers: \"prime\", \"composite\"")
		print("Quadratic Formula: \"roots\", \"quadratic formula\", \"quadForm\"")
		print("Slope: *no shortcuts*")
		print("Square root: \"sqrt\"")
		print("Subtract Fractions: \"subfrac\"")
		print("Subtraction: \"minus\", \"subtract\", \"-\", \"sub\"")
		print("")
		
#start of sections

#quadratic formula
	if equation == "quadratic formula" or equation == "roots" or equation == "quadform":
		qfa = int(input("Enter A: "))
		qfb = int(input("Enter B: "))
		qfc = int(input("Enter C: "))
		qfradicand = qfb * qfb
		qfradicand = qfradicand + -4*qfa*qfc
		denominator = 2 * qfa
		try:
			qftestRT = math.sqrt(qfradicand)
			qfradicand = qftestRT
			qfroot1 = 0-qfb + qfradicand
			qfroot1 = fractioner(int(qfroot1), int(denominator))
			qfroot2 = 0-qfb - qfradicand
			qfroot2 = fractioner(int(qfroot2),int(denominator))
				
		except Exception as exception0:
			qfroot1 = "(" + str(0-qfb) + " + " + " sqrt " + str(qfradicand) + ") / " + str(denominator)
			qfroot2 = "(" + str(0-qfb) + " - " + " sqrt " + str(qfradicand) + ") / " + str(denominator)
		print(qfroot1)
		print(qfroot2)

#factors
	if equation == "factors" or equation == "find factors" :
		theNumberTXT = input("Type the number: ")
		print(findFactors(int(theNumberTXT)))
	
#Prime and composite numbers	
	if equation == "prime numbers" or equation == "composite numbers"  or equation == "composite" or equation == "prime":
		theNumberTXT = input("Type the number: ")
		theNumber = int(theNumberTXT)
		for x in range(2, theNumber):
			if x != theNumber:
				theNextNumber = theNumber%x
			if theNextNumber == 0:
				break
		if theNextNumber == 0:
			print("This is a composite number")
		else:
			print("This is a prime number")
	

#distance	
	if equation == "distance" or equation == "length":
		X1TXT = input("X1: ")
		X1 = int(X1TXT)
		Y1TXT = input("Y1: ")
		Y1 = int(Y1TXT)
		X2TXT = input("X2: ")
		X2 = int(X2TXT)
		Y2TXT = input("Y2: ")
		Y2 = int(Y2TXT)
		X = (X2 - X1)**2
		Y = (Y2 - Y1)**2
		answer = X+Y
		sqrtAnswer = sqrt(answer)
		checker = isinstance(sqrtAnswer, int)
		if checker == True:
			print(sqrtAnswer)
		if checker == False:
			print(reduceRoots(answer))
	

#midpoint
	if equation == "midpoint" or equation == "mid":
		X1TXT = input("X1: ")
		X1 = int(X1TXT)
		Y1TXT = input("Y1: ")
		Y1 = int(Y1TXT)
		X2TXT = input("X2: ")
		X2 = int(X2TXT)
		Y2TXT = input("Y2: ")
		Y2 = int(Y2TXT)
		XFirstPart = (X1+X2)
		YFirstPart = (Y1+Y2)
		X = fractioner(XFirstPart, 2)
		Y = fractioner(YFirstPart, 2)
		print(str(X) + "," + str(Y))
	

#slope	
	if equation == "slope":
		X1TXT = input("X1: ")
		X1 = int(X1TXT)
		Y1TXT = input("Y1: ")
		Y1 = int(Y1TXT)
		X2TXT = input("X2: ")
		X2 = int(X2TXT)
		Y2TXT = input("Y2: ")
		Y2 = int(Y2TXT)
		Y = Y2-Y1
		X = X2-X1
		gcdXY = math.gcd(Y,X)
		YFrac = Y/gcdXY
		XFrac = X/gcdXY
		if XFrac < 0 and YFrac < 0:
			XFrac = XFrac * -1
			YFrac = YFrac * -1
		YFracString = str(YFrac)
		XFracString = str(XFrac)
		if XFrac == 1:
			print(YFrac)
		if XFrac != 1:
			print(str(YFracString) + "/" + str(XFracString))
	

#squareroot
	if equation == "squareroot" or equation == "sqrt" or equation == "square root":
		numberTXT = input("Type the number: ")
		number = int(numberTXT)
		if number < 0:
			print("This number cannot be rooted")
		if number > 0:
			numberRTD = math.sqrt(number)
			checker = math.ceil(numberRTD)
			if numberRTD - checker == 0:
				print(numberRTD)
			else:
				print(reduceRoots(number))
		
#alphabetical order	
	if equation == "alphabetical order" or equation == "alphaorder":
		while vari < 10:
			alphaPhrase = input("Type your phrases in 1 at a time: ")
			if alphaPhrase == "done":
				print(sorted(alphaOrderArr))
				alphaOrderArr.clear()
				break
			alphaOrderArr.append(alphaPhrase)
			print(sorted(alphaOrderArr))
	

#Add Fractions
	if equation == "fracadd" or equation == "add fractions" or equation == "fraction add" or equation == "addfrac":
		Nu1TXT = input("Numerator1: ")
		Nu1 = int(Nu1TXT)
		deno1TXT = input("Denominator1: ")
		deno1 = int(deno1TXT)
		Nu2TXT = input("Numerator2: ")
		Nu2 = int(Nu2TXT)
		deno2TXT = input("Denominator2: ")
		deno2 = int(deno2TXT)
		FracAddLcm = lcm(deno1, deno2)
		FracAddMul1 = FracAddLcm/deno1
		FracAddMul2 = FracAddLcm/deno2
		FracAddNu1 = Nu1 * FracAddMul1
		FracAddNu2 = Nu2 * FracAddMul2
		FracAddDeno = int(FracAddLcm)
		FracAddNu = int(FracAddNu1 + FracAddNu2)
		FracAddOut = str(FracAddNu) + "/" + str(FracAddDeno)
		FracAddRedOut = str(fractioner(FracAddNu, FracAddDeno))
		print(FracAddOut)
		if FracAddOut != FracAddRedOut:
			print(FracAddRedOut)
		
	

#Subtract Fractions
	if equation == "fracsub" or equation == "subtract fractions" or equation == "subfrac":
		Nu1TXT = input("Numerator1: ")
		Nu1 = int(Nu1TXT)
		deno1TXT = input("Denominator1: ")
		deno1 = int(deno1TXT)
		Nu2TXT = input("Numerator2: ")
		Nu2 = int(Nu2TXT)
		deno2TXT = input("Denominator2: ")
		deno2 = int(deno2TXT)
		FracSubLcm = lcm(deno1, deno2)
		FracSubMul1 = FracSubLcm/deno1
		FracSubMul2 = FracSubLcm/deno2
		FracSubNu1 = Nu1 * FracSubMul1
		FracSubNu2 = Nu2 * FracSubMul2
		FracSubDeno = int(FracSubLcm)
		FracSubNu = int(FracSubNu1 - FracSubNu2)
		FracSubOut = str(FracSubNu) + "/" + str(FracSubDeno)
		FracSubRedOut =  str(fractioner(FracSubNu, FracSubDeno))
		print(FracSubOut)
		if FracSubOut != FracSubRedOut:
			print(FracSubRedOut)
	
#Multiply Fractions	
	if equation == "fracmult" or equation == "multiply fractions" or equation == "multfrac":
		Nu1TXT = input("Numerator1: ")
		Nu1 = int(Nu1TXT)
		deno1TXT = input("Denominator1: ")
		deno1 = int(deno1TXT)
		Nu2TXT = input("Numerator2: ")
		Nu2 = int(Nu2TXT)
		deno2TXT = input("Denominator2: ")
		deno2 = int(deno2TXT)
		FracMultNu = int(Nu1 * Nu2)
		FracMultDeno = int(deno1 * deno2)
		FracMultOut = str(FracMultNu) + "/" + str(FracMultDeno)
		FracMultRedOut = str(fractioner(FracMultNu, FracMultDeno))
		print(FracMultOut)
		if FracMultOut != FracMultRedOut:
			print(FracMultRedOut)
	

#Divide Fractions	
	if equation == "fracdiv" or equation == "divide fractions" or equation == "divfrac": 
		Nu1TXT = input("Numerator1: ")
		Nu1 = int(Nu1TXT)
		deno1TXT = input("Denominator1: ")
		deno1 = int(deno1TXT)
		Nu2TXT = input("Numerator2: ")
		Nu2 = int(Nu2TXT)
		deno2TXT = input("Denominator2: ")
		deno2 = int(deno2TXT)
		FracDivNu = int(Nu1 * deno2)
		FracDivDeno = int(deno1 * Nu2)
		FracDivOut = str(FracDivNu) + "/" + str(FracDivDeno)
		FracDivRedOut = str(fractioner(FracDivNu, FracDivDeno))
		print(FracDivOut)
		if FracDivOut != FracDivRedOut:
			print(FracDivRedOut)

	
#Lowest common multiple	
	if equation == "lcm" or equation == "lowest common multiple":
		firstNumberTXT = input("Type the first number you want to calculate: ")
		firstNumber = int(firstNumberTXT)
		secondNumberTXT = input("Type the second number you want to calculate: ")
		secondNumber = int(secondNumberTXT)
		print(lcm(firstNumber, secondNumber))
	
#Greatest common divisor	
	if equation == "gcd" or equation == "greatest common divisor":
		firstNumberTXT = input("Type the first number you want to calculate: ")
		firstNumber = int(firstNumberTXT)
		secondNumberTXT = input("Type the second number you want to calculate: ")
		secondNumber = int(secondNumberTXT)
		print(math.gcd(firstNumber, secondNumber))
	
#add	
	if equation == "addition" or equation == "add" or equation == "+":
		firstNumberTXT = input("Type the first number you want to calculate: ")
		firstNumber = int(firstNumberTXT)
		secondNumberTXT = input("Type the second number you want to calculate: ")
		secondNumber = int(secondNumberTXT)
		print(firstNumber+secondNumber)
	
#subtract	
	if equation == "subtraction" or equation == "minus" or equation == "subtract" or equation == "-" or equation == "sub":
		firstNumberTXT = input("Type the first number you want to calculate: ")
		firstNumber = int(firstNumberTXT)
		secondNumberTXT = input("Type the second number you want to calculate: ")
		secondNumber = int(secondNumberTXT)
		print(firstNumber - secondNumber)
	
#multiply	
	if equation == "multiplication" or equation == "multiply" or equation == "times" or equation == "*":
		firstNumberTXT = input("Type the first number you want to calculate: ")
		firstNumber = int(firstNumberTXT)
		secondNumberTXT = input("Type the second number you want to calculate: ")
		secondNumber = int(secondNumberTXT)
		print(firstNumber * secondNumber)
	
#divide	
	if equation == "division" or equation == "divide" or equation == "/":
		firstNumberTXT = input("Type the first number you want to calculate: ")
		firstNumber = int(firstNumberTXT)
		secondNumberTXT = input("Type the second number you want to calculate: ")
		secondNumber = int(secondNumberTXT)
		d = math.gcd(firstNumber, secondNumber)
		firstNumberFraction = firstNumber/d
		secondNumberFraction = secondNumber/d
		de = Decimal(firstNumber/float(secondNumber))
		print(str(firstNumberFraction) + "/" + str(secondNumberFraction) + "(" + str(de) + ")" )
	
#power	
	if equation == "power" or equation == "to the power of":
		firstNumberTXT = input("Type the first number you want to calculate: ")
		firstNumber = int(firstNumberTXT)
		secondNumberTXT = input("Type the second number you want to calculate: ")
		secondNumber = int(secondNumberTXT)
		print(firstNumber ** secondNumber)
	
#end program	
	if equation == "quit" or equation == "q" or equation == "done":
		break
