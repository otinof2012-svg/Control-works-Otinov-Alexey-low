import math

running=True
while running
    num1 = int(input("Введите первое число:"))
    num2 = int(input("Введите второе число(или степень):"))
    operation = input("Введите операцию (+, -, *, /, %, Степень, log):")
    if operation=="+":
        result = num1+num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "%":
        result = num1/num2*100
    elif operation == "Степень":
        result = num1 ** num2
    elif operation == "log":
        result = math.log(num1, num2)
    else:
        print("Ошибка: Недопустимая операция.")
        
    print("Результат", result)
    
    again = input("Продолжить? (+ -да, другое-нет):")
    if again != "+":
        running = False
        
print("Программа завершена")
