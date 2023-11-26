def multiply_large_numbers(num1, num2):
    # Convert the input numbers to integers
    int_num1 = int(num1)
    int_num2 = int(num2)
    
    product = int_num1 * int_num2
    
    return product

#Solution
num1 = "3141592653589793238462643383279502884197169399375105820974944592"
num2 = "2718281828459045235360287471352662497757247093699959574966967627"

result = multiply_large_numbers(num1, num2)
print(result)