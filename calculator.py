
num1 = float(input("Enter first number :"))
op = input("choose operator  (+,-,*,/ ) :")
num2 = float(input("Enter second number : "))

if op == "+" :
	 print("result = ", num1 + num2)
	 
elif op == "-" :
	print("Result = " , num1 - num2)
elif op == "*" :
	print("Result = " , num1 * num2)
elif op == "/" :
	print("Result = " , num1 / num2)
	
else:
	print("Invalid opreation")