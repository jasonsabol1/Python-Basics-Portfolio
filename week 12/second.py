def calculate_factorial(n):
  return 1 if (n==1 or n==0) else n * calculate_factorial(n-1)