def result_print(sum_result):

    print("Ответ: " + str(sum_result))

def sum_number():
    n = int(input("Введите число: "))
    number = ""
    while n > 0:
        number = str(n % 2) + number
        n = n // 2

    result_print(number) 
       
        
 

sum_number()