firstNum = 0

secondNum = 0

operation = ""

# This function takes two numbers, adds them together, and returns the new value
def addition(firstNumber, secondNumber):
	total = float(firstNumber) + float(secondNumber)

	return total

# This function takes two numbers, subracts them, and returns the new value
def subtraction(firstNumber, secondNumber):
    difference = float(firstNumber) - float(secondNumber)
	

    return difference

# This function takes two numbers, multiplies them, and returns the new value
def multiplication(firstNumber, secondNumber):
    newNumber = float(firstNumber) * float(secondNumber)

    return newNumber

# This function takes two numbers divides them, and returns the new value
def division(firstNumber, secondNumber):
    newNumber = float(firstNumber) / float(secondNumber)

    return newNumber

# This function takes two numbers, divides them, and returns the remainder
def modulus(firstNumber, secondNumber):
	newNumber = float(firstNumber) % float(secondNumber)

	return newNumber

# This function takes two numbers, raises the first number by the second number, and returns the new value
def exponent(firstNumber, secondNumber):
	newNumber = float(firstNumber) ** float(secondNumber)

	return newNumber

# This function allows the user to input two numbers and the operation they wish and then calulates the value
def main():
	firstNum = input("Please input a number: ")
	
	secondNum = input("Please input a second number: ")
	
	operation = input("Type 'add', 'sub', 'mult', 'div', 'mod', or 'exp' for operation: ")

	if operation == 'add':
		number = addition(firstNum, secondNum)
		print(number)

	elif operation == 'sub':
		number = subtraction(firstNum, secondNum)
		print(number)

	elif operation == 'mult':
		number = multiplication(firstNum, secondNum)
		print(number)

	elif operation == 'div':
		number = division(firstNum, secondNum)
		print(number)

	elif operation == 'mod':
		number = modulus(firstNum, secondNum)
		print(number)

	elif operation == 'exp':
		number = exponent(firstNum, secondNum)
		print(number)

main()