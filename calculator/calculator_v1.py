numA = 0
numB = 0
result = 0
operation = ''

numA = int(input("First number: "))
operation = input("The operation type: ")
numB = int(input("Second number: "))

if operation == '+':
    resulato = numA + numB

elif operation == '-':
    result = numA - numB

elif operation == '*':
    result = numA * numB

elif operation == '/':
    if numB == 0:
        print("Error: Division by zero!")
    else:
        result = numA / numB

else:
    result = "ERROR: Invalid operation"

print(result)
