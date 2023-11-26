num_1 = input("Enter first number: ")
num_2 = input("Enter second number: ")
num_1_int = int(num_1)
num_2_int = int(num_2)
while num_2_int == 0:
  print("please re-enter, cannot divide by zero.")
  num_1 = input("Enter first number: ")
  num_2 = input("Enter second number: ")
  num_1_int = int(num_1)
  num_2_int = int(num_2)
addition_output = (num_1_int + num_2_int)
subtraction_output = (num_1_int - num_2_int)
multiplication_output = (num_1_int * num_2_int)
division_output = (num_1_int / num_2_int)  
print("Addition: ", addition_output)
print("Subtraction: ", subtraction_output)
print("Multiplication: ", multiplication_output)
print("Division: ", division_output)




