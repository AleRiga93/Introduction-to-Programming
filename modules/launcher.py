from input import user_numbers
from processing import summ, diff, prod, quot
from output import output_result

def launcher ():
    num1, num2 = user_numbers()
    summ_result = summ(num1, num2)
    diff_result = diff(num1, num2)
    prod_result = prod(num1, num2)
    quot_result = quot(num1, num2)
    

    output_result (num1, num2, summ_result, diff_result, prod_result, quot_result)

launcher()


