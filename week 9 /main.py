from random import random
with open('fruits.txt', 'r') as file:
  file_contents = file.read()
  lines = file_contents.split('\n')
  fruit_dict={}
  for line in lines:
    fruit_dict[line.strip()] = random() * 10

fruit_name = input(" What fruit would you like to check the price for? ")
if fruit_name in fruit_dict: 
  print("The price of your fruit is: ", fruit_dict[fruit_name])
else: 
  print("Sorry, we don't have data on this fruit.")

