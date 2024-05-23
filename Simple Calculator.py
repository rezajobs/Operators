while True:
    number1 = int(input('say a number : '))
    number2 = int(input('say a number : '))

    calculator = input('Choose an operation (+, -, *, /):')
    if calculator == '+':
        print('Addition :',number1+number2)
    elif calculator == '-':
        print('Subtraction :', number1-number2)
    elif calculator == '*':
        print('Multiplication :', number1*number2)
    elif calculator == '/':
        if number2 == 0:
            print('Error: Division by zero is not allowed.')
        else:
                print('Division:', number1 / number2)
    else:
            print('Invalid operation. Please choose +, -, *, or /.')
   

    continue_calculation = input('Do you want to perform another calculation? (yes/no): ').strip().lower()
    if continue_calculation != 'yes':
         break
