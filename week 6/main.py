
def numbers(x_int):
  if x_int > 0:
    str_1='Your number is positive'
  if x_int < 0:
    str_1='Your number is negative'
  if x_int == 0:
    str_1='Your number is zero'
  if x_int % 2 == 0:
    str_2='Your number is even'
  else:
    str_2="Your number is odd"
  return str_1, str_2
x = input("Enter number here: ")
x_int = int(x)
str_1, str_2=numbers(x_int)
print(str_1)
print(str_2)
