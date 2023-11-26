def square_function(x):
  x_int = int(x)
  y=x_int*x_int
  return y
x = input("Enter Number: ")
y=square_function(x) 
y_str=str(y)
print("Your number squared: " + y_str)
