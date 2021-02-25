#fix solve because of decimals

from fractions import gcd
from decimal import *
import math

alphaOrderArr = []
vari = 1
varia = 2
while vari < 10:
	def lcm(k,l):
                return k*l/(gcd(k,l))

	def sqrt(numberToBeRooted):
        	return numberToBeRooted**0.5
	
	def fractioner(numerator, denominator):
        	theGCD = gcd(numerator, denominator)
        	finalNumerator = numerator/theGCD
        	finalDenominator = denominator/theGCD
        	if finalDenominator == 1:
                	return finalNumerator
        	if finalDenominator != 1:
                	return str(finalNumerator) + "/" + str(finalDenominator)

	equation = raw_input("What would you like to do? (Type man or manual for a list of operators): ")
	if equation == "Man" or equation == "Manual" or equation == "man" or equation == "manual":
		print("Slope")
		print("Midpoint")
		print("Square Root")
		print("Alphabetical Order")
		print("Add Fractions")
		print("Subtract Fractions")
		print("Multiply Fractions")
		print("Divide Fractions")
		print("Check if equations are equal (not trustworthy)")
		print("Lowest Common Multiple")
		print("Greatest Common Factor")
		print("Addition")
		print("Subtraction")
		print("Multiplication")
		print("Division")
		print("Power")
	if equation == "distance" or equation == "length":
		X1 = input("X1: ")
                Y1 = input("Y1: ")
                X2 = input("X2: ")
                Y2 = input("Y2: ")
		X = (X1 - X2)**2
                Y = (Y1 - Y2)**2
                answer = X+Y
		sqrtAnswer = sqrt(answer)
		checker = isinstance(sqrtAnswer, int)
		if answer < 0:
			print("sqrt", answer)
		if answer > 0 and checker == False:
			print("sqrt", answer)
		if answer > 0 and checker == True:
			print(sqrtAnswer)
	if equation == "midpoint":
		X1 = input("X1: ")
                Y1 = input("Y1: ")
                X2 = input("X2: ")
                Y2 = input("Y2: ")
		XFirstPart = (X1+X2)
		YFirstPart = (Y1+Y2)
		X = fractioner(XFirstPart, 2)
		Y = fractioner(YFirstPart, 2)
		print(str(X) + "," + str(Y))
	if equation == "slope" or equation == "Slope":
		X1 = input("X1: ")
                Y1 = input("Y1: ")
                X2 = input("X2: ")
                Y2 = input("Y2: ")
		Y = Y2-Y1
		X = X2-X1
		gcdXY = gcd(Y,X)
		YFrac = Y/gcdXY
		XFrac = X/gcdXY
		YFracString = str(YFrac)
		XFracString = str(XFrac)
		if XFrac == 1:
			print(YFrac)
		if XFrac != 1:
			print(str(YFracString) + "/" + str(XFracString))
	if equation == "squareroot" or equation == "sqrt" or equation == "SQRT":
		number = input("Type the number: ")
		if number < 0:
			print("This number cannot be rooted")
		if number > 0:
			print(math.sqrt(number))
	if equation == "root" or equation == "Root":
		numberBeingRooted = input("what number would you like to root?: ")
                numberBeingRootedTo = input("what number would you like to root to?: ")
		def root(RootNumberOne, RootNumberTwo):
			RealRootNumberTwo = (1. / float(RootNumberTwo))
			return(float(RootNumberOne) ** float(RealRootNumberTwo))
		print(root(numberBeingRooted, numberBeingRootedTo))
	if equation == "AlphaOrder" or equation == "Alphabetical Order" or equation == "alphaOrder" or equation == "alphabetical order":
		while vari < 10:
			alphaPhrase = raw_input("Type your phrases in 1 at a time: ")
			if alphaPhrase == "done":
				print(sorted(alphaOrderArr))
				break
			alphaOrderArr.append(alphaPhrase)
			print(sorted(alphaOrderArr))
	if equation == "FracAdd" or equation == "Add Fractions" or equation == "Fraction add":
                Nu1 = input("Numerator1: ")
                deno1 = input("Denominator1: ")
                Nu2 = input("Numerator2: ")
                deno2 = input("Denominator2: ")
                FracAddLcm = lcm(deno1, deno2)
                FracAddMul1 = FracAddLcm/deno1
                FracAddMul2 = FracAddLcm/deno2
                FracAddNu1 = Nu1 * FracAddMul1
                FracAddNu2 = Nu2 * FracAddMul2
                FracAddDeno = FracAddLcm
                FracAddNu = FracAddNu1 + FracAddNu2
                print(str(FracAddNu) + "/" + str(FracAddDeno))
	if equation == "FracSub" or equation == "Fraction subtraction" or equation == "Subtract fractions":
                Nu1 = input("Numerator1: ")
                deno1 = input("Denominator1: ")
                Nu2 = input("Numerator2: ")
                deno2 = input("Denominator2: ")
                FracSubLcm = lcm(deno1, deno2)
                FracSubMul1 = FracSubLcm/deno1
                FracSubMul2 = FracSubLcm/deno2
                FracSubNu1 = Nu1 * FracSubMul1
                FracSubNu2 = Nu2 * FracSubMul2
                FracSubDeno = FracSubLcm
                FracSubNu = FracSubNu1 - FracSubNu2
                print(str(FracSubNu) + "/" + str(FracSubDeno))
	if equation == "FracMult" or equation == "Fraction Multiply" or equation == "Multiply fractions":
		Nu1 = input("Numerator1: ")
                deno1 = input("Denominator1: ")
                Nu2 = input("Numerator2: ")
                deno2 = input("Denominator2: ")
                FracMultNu = Nu1 * Nu2
                FracMultDeno = deno1 * deno2
                print(str(FracMultNu) + "/" + str(FracMultDeno))
	if equation == "FracDiv" or equation == "Fraction Division" or equation == "Fraction divide" or equation == "divide fractions": 
		Nu1 = input("Numerator1: ")
                deno1 = input("Denominator1: ")
                Nu2 = input("Numerator2: ")
                deno2 = input("Denominator2: ")
                FracDivNu = Nu1 * deno2
                FracDivDeno = deno1 * Nu2
                print(str(FracDivNu) + "/" + str(FracDivDeno))
	if equation == "check":
		firstNumberTxt = input("Type the first number you want to calculate: ")
		secondNumberTxt = input("Type the second number you want to calculate: ")
		print(firstNumberTxt == secondNumberTxt)
	if equation == "lcm" or equation == "lowest common multiple":
		firstNumberTxt = input("Type the first number you want to calculate: ")
		secondNumberTxt = input("Type the second number you want to calculate: ")
		print(lcm(firstNumberTxt, secondNumberTxt))
	if equation == "gcd" or equation == "greatest common divisor" or equation == "gcf" or equation == "greatest common factor":
		firstNumberTxt = input("Type the first number you want to calculate: ")
		secondNumberTxt = input("Type the second number you want to calculate: ")
		print(gcd(firstNumberTxt, secondNumberTxt))
	if equation == "addition" or equation == "add" or equation == "+":
		firstNumberTxt = input("Type the first number you want to calculate: ")
		secondNumberTxt = input("Type the second number you want to calculate: ")
		print(firstNumberTxt+secondNumberTxt)
	if equation == "subtraction" or equation == "minus" or equation == "subtract" or equation == "-":
		firstNumberTxt = input("Type the first number you want to calculate: ")
		secondNumberTxt = input("Type the second number you want to calculate: ")
		print(firstNumberTxt - secondNumberTxt)
	if equation == "multiplication" or equation == "multiply" or equation == "times" or equation == "*":
		firstNumberTxt = input("Type the first number you want to calculate: ")
		secondNumberTxt = input("Type the second number you want to calculate: ")
		print(firstNumberTxt * secondNumberTxt)
	if equation == "division" or equation == "divide" or equation == "/":
		firstNumberTxt = input("Type the first number you want to calculate: ")
		secondNumberTxt = input("Type the second number you want to calculate: ")
		d = gcd(firstNumberTxt, secondNumberTxt)
		firstNumberFraction = firstNumberTxt/d
		secondNumberFraction = secondNumberTxt/d
		de = Decimal(firstNumberTxt/float(secondNumberTxt))
		print(str(firstNumberFraction) + "/" + str(secondNumberFraction) + "(" + str(de) + ")" )
	if equation == "power" or equation == "to the power of":
		firstNumberTxt = input("Type the first number you want to calculate: ")
		secondNumberTxt = input("Type the second number you want to calculate: ")
		print(firstNumberTxt ** secondNumberTxt)
	if equation == "quit" or equation == "q" or equation == "exit" or equation == "done":
		
