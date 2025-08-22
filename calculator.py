num1=float(input('Ingresa un primer número: '))
num2= float(input('Ingresa un segundo número: '))


operación=input('Elige una operación:')
print('+,-,/,*')

if operación=='+':
   print(num1+num2)
elif operación=='-':
    print(num1-num2)
elif operación=='/':
    if num2!=0:
        print(num1/num2)
    else:
        print('No se puede dividir entre 0')
elif operación=='*':
    print(num1*num2)

