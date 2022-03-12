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
	def removeDecimal(num):
		if(math.ceil(num) == num):
			output = int(num)
		else:
			output = num
		return output
	
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
		elif finalDenominator == 0 or finalNumerator == 0:
			return 0
		elif finalDenominator != 1:
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
	
	def decToFrac(num):
		wholeNumber = math.floor(num)
		
		count = 0
		counter = Decimal(str(num)) - Decimal(str(math.floor(num)))
		while counter / math.ceil(counter) != 1:
			count = count + 1
			counter = counter * 10
		digitsADecimal = count
		
		numerator = int(counter)
		i = 1
		denominator = 1
		while i <= digitsADecimal:
			denominator = denominator * 10
			i = i + 1
		wholeNumber = wholeNumber * denominator
		numerator = numerator + wholeNumber
		return fractioner(numerator, denominator)




	equation = input("What would you like to do? (Type man or manual for a list of operators): ")
	
	equation = equation.lower()
	
	
	
	if equation == "man" or equation == "manual":
	
		print("")
		print("Manual Shortcuts")
		print("Add Fractions")
		print("Addition")
		print("Alphabetical Order")
		print("Decimal To Fraction")
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


	elif equation == "manual shortcuts" or equation == "mshort":
		
		print("")
		print ("All Manual Shorcuts Or Short Forms:")
		print("")
		print("Manual Shortcuts: \"MShort\"")
		print("Add Fractions: \"fracadd\"")
		print("Addition: \"add\", \"+\"")
		print("Alphabetical Order: \"alphaorder\"")
		print("Decimal to Fraction: \"dec2frac\", \"ConvertFraction\"")
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
	elif equation == "quadratic formula" or equation == "roots" or equation == "quadform":
		try:
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

			except Exception as exception01:
				qfroot1 = "(" + str(0-qfb) + " + " + " sqrt " + str(qfradicand) + ") / " + str(denominator)
				qfroot2 = "(" + str(0-qfb) + " - " + " sqrt " + str(qfradicand) + ") / " + str(denominator)
			print(qfroot1)
			print(qfroot2)
		except Exception as exception0:
			print("One or more invalid inputs were entered\n")

#factors
	elif equation == "factors" or equation == "find factors" :
		try:			
			theNumber = int(input("Type the number: "))
			print(findFactors(theNumber))
		except Exception as exception1:
			print("One or more invalid inputs were entered\n")
	
#Prime and composite numbers	
	elif equation == "prime numbers" or equation == "composite numbers"  or equation == "composite" or equation == "prime":
		try:
			theNumber = int(input("Type the number: "))
			for x in range(2, theNumber):
				if x != theNumber:
					theNextNumber = theNumber%x
				if theNextNumber == 0:
					break
			if theNextNumber == 0:
				print("This is a composite number")
			else:
				print("This is a prime number")
		except Exception as exception2:
			print("One or more invalid inputs were entered\n")
	

#distance	
	elif equation == "distance" or equation == "length":
		try:
			X1 = int(input("X1: "))
			Y1 = int(input("Y1: "))
			X2 = int(input("X2: "))
			Y2 = int(input("Y2: "))
			X = (X2 - X1)**2
			Y = (Y2 - Y1)**2
			answer = X+Y
			sqrtAnswer = sqrt(answer)
			checker = isinstance(sqrtAnswer, int)
			if checker == True:
				print(sqrtAnswer)
			if checker == False:
				print(reduceRoots(answer))
		except Exception as exception3:
			print("One or more invalid inputs were entered\n")
	

#midpoint
	elif equation == "midpoint" or equation == "mid":
		try:
			X1 = int(input("X1: "))
			Y1 = int(input("Y1: "))
			X2 = int(input("X2: "))
			Y2 = int(input("Y2: "))
			XFirstPart = (X1+X2)
			YFirstPart = (Y1+Y2)
			X = fractioner(XFirstPart, 2)
			Y = fractioner(YFirstPart, 2)
			print(str(X) + "," + str(Y))
		except Exception as exception4:
			print("One or more invalid inputs were entered\n")
	
#slope	
	elif equation == "slope":
		try:
			X1 = int(input("X1: "))
			Y1 = int(input("Y1: "))
			X2 = int(input("X2: "))
			Y2 = int(input("Y2: "))
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
		except Exception as exception5:
			print("One or more invalid inputs were entered\n")
	

#squareroot
	elif equation == "squareroot" or equation == "sqrt" or equation == "square root":
		try:
			number = Decimal(input("Type the number: "))
			if number < 0:
				print("This number cannot be rooted")
			elif number != math.ceil(number):
				print(math.sqrt(number))
			elif number > 0:
				numberRTD = math.sqrt(number)
				if numberRTD - math.ceil(numberRTD) == 0:
					print(removeDecimal(numberRTD))
				else:
					print(reduceRoots(number))
			
		except Exception as exception6:
			print("One or more invalid inputs were entered\n")
		
#alphabetical order	
	elif equation == "alphabetical order" or equation == "alphaorder":
		while vari < 10:
			alphaPhrase = input("Type your phrases in 1 at a time ('/done' to exit): ")
			if alphaPhrase == "/done":
				print(sorted(alphaOrderArr))
				alphaOrderArr.clear()
				break
			alphaOrderArr.append(alphaPhrase)
			print(sorted(alphaOrderArr))
	

#Add Fractions
	elif equation == "fracadd" or equation == "add fractions" or equation == "fraction add" or equation == "addfrac":
		try:
			Nu1 = int(input("Numerator1: "))
			deno1 = int(input("Denominator1: "))
			Nu2 = int(input("Numerator2: "))
			deno2 = int(input("Denominator2: "))
			if deno1 == 0:
				print(fractioner(Nu2, deno2))
			elif deno2 == 0:
				print(fractioner(Nu1, deno1))
			else:
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
		except Exception as exception7:
			print("One or more invalid inputs were entered\n")
		
	

#Subtract Fractions
	elif equation == "fracsub" or equation == "subtract fractions" or equation == "subfrac":
		try:
			Nu1 = int(input("Numerator1: "))
			deno1 = int(input("Denominator1: "))
			Nu2 = int(input("Numerator2: "))
			deno2 = int(input("Denominator2: "))
			if deno1 == 0:
				print(fractioner(Nu2, deno2))
			elif deno2 == 0:
				print(fractioner(Nu1, deno1))
			else:
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
		except Exception as exception8:
			print("One or more invalid inputs were entered\n")
				
	
#Multiply Fractions	
	elif equation == "fracmult" or equation == "multiply fractions" or equation == "multfrac":
		try:
			Nu1 = int(input("Numerator1: "))
			deno1 = int(input("Denominator1: "))
			Nu2 = int(input("Numerator2: "))
			deno2 = int(input("Denominator2: "))
			FracMultNu = int(Nu1 * Nu2)
			FracMultDeno = int(deno1 * deno2)
			FracMultOut = str(FracMultNu) + "/" + str(FracMultDeno)
			FracMultRedOut = str(fractioner(FracMultNu, FracMultDeno))
			print(FracMultOut)
			if FracMultOut != FracMultRedOut:
				print(FracMultRedOut)
		except Exception as exception9:
			print("One or more invalid inputs were entered\n")
	

#Divide Fractions	
	elif equation == "fracdiv" or equation == "divide fractions" or equation == "divfrac": 
		try:
			Nu1 = int(input("Numerator1: "))
			deno1 = int(input("Denominator1: "))
			Nu2 = int(input("Numerator2: "))
			deno2 = int(input("Denominator2: "))
			FracDivNu = int(Nu1 * deno2)
			FracDivDeno = int(deno1 * Nu2)
			FracDivOut = str(FracDivNu) + "/" + str(FracDivDeno)
			FracDivRedOut = str(fractioner(FracDivNu, FracDivDeno))
			print(FracDivOut)
			if FracDivOut != FracDivRedOut:
				print(FracDivRedOut)
		except Exception as exception10:
			print("One or more invalid inputs were entered\n")

	
#Lowest common multiple	
	elif equation == "lcm" or equation == "lowest common multiple":
		try:
			firstNumber = int(input("Type the first number you want to calculate: "))
			secondNumber = int(input("Type the second number you want to calculate: "))
			print(lcm(firstNumber, secondNumber))
		except Exception as exception11:
			print("One or more invalid inputs were entered\n")
	
#Greatest common divisor	
	elif equation == "gcd" or equation == "greatest common divisor":
		try:
			firstNumber = int(input("Type the first number you want to calculate: "))
			secondNumber = int(input("Type the second number you want to calculate: "))
			print(math.gcd(firstNumber, secondNumber))
		except Exception as exception12:
			print("One or more invalid inputs were entered\n")			
			
#add	
	elif equation == "addition" or equation == "add" or equation == "+":
		try:
			firstNumber = Decimal(input("Type the first number you want to calculate: "))
			secondNumber = Decimal(input("Type the second number you want to calculate: "))
			print(removeDecimal(firstNumber + secondNumber))
		except Exception as exception13:
			print("One or more invalid inputs were entered\n")
	
#subtract	
	elif equation == "subtraction" or equation == "minus" or equation == "subtract" or equation == "-" or equation == "sub":
		try:
			firstNumber = Decimal(input("Type the first number you want to calculate: "))
			secondNumber = Decimal(input("Type the second number you want to calculate: "))
			print(removeDecimal(firstNumber - secondNumber))
		except Exception as exception14:
			print("One or more invalid inputs were entered\n")
	
#multiply	
	elif equation == "multiplication" or equation == "multiply" or equation == "times" or equation == "*":
		try:
			firstNumber = Decimal(input("Type the first number you want to calculate: "))
			secondNumber = Decimal(input("Type the second number you want to calculate: "))
			print(removeDecimal(firstNumber * secondNumber))
		except Exception as exception15:
			print("One or more invalid inputs were entered\n")
	
#divide	
	elif equation == "division" or equation == "divide" or equation == "/":
		try:
			firstNumber = Decimal(input("Type the first number you want to calculate: "))
			secondNumber = Decimal(input("Type the second number you want to calculate: "))
			de = (Decimal(str(firstNumber))/Decimal(str(secondNumber)))
			if math.ceil(firstNumber) == firstNumber and math.ceil(secondNumber) == secondNumber:
				d = math.gcd(removeDecimal(firstNumber), removeDecimal(secondNumber))
				firstNumberFraction = removeDecimal(firstNumber/d)
				secondNumberFraction = removeDecimal(secondNumber/d)
				print(str(firstNumberFraction) + "/" + str(secondNumberFraction) + "(" + str(de) + ")" )
			else:
				print(str(decToFrac(de)) + "(" + str(de) + ")")
		except Exception as exception16:
			print("One or more invalid inputs were entered\n")
	
#power	
	elif equation == "power" or equation == "to the power of":
		try:
			firstNumber = Decimal(input("What is the coefficient?: "))
			secondNumber = Decimal(input("What is the exponent?: "))
			print(removeDecimal(firstNumber ** secondNumber))
		except Exception as exception17:
			print("One or more invalid inputs were entered\n")
			
#decimalToFraction
	elif equation == "decimaltofraction" or equation == "dec2frac" or equation == "convertfraction":
		try:
			num = Decimal(input("Type the decimal: "))
			print(decToFrac(num))
		except Exception as exception18:
			print("One or more invalid inputs were entered\n")

#favorites
	elif equation == "changeFavorites" or equation  == "favorites":
		try:
			fchq = int(input("Type what preset you would like to change (1, 2, 3, 4, 5): "))
			if fchq == 1:
				
		except Exception as exception19:
			print("One or more invalid inputs were entered\n")

			
#end program	
	elif equation == "quit" or equation == "q" or equation == "done":
		break
		
#no function
	else:
		print("This program cannot complete that function at the time \nIf you have a request for a new function, please leave it on the issues page of the github repo (https://github.com/LMJD4/CalculatorForAllCalculationsAndFomulas/issues)\n")
