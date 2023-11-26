Fruit_Dict= {"Apple": 1.31, "Orange": 1.51, "Peach": 0.81, "Pear": 0.53, "Blueberry": 2.16}
x= input("What fruit price would you like to know? ")
def fruit_function(x):
  if x == "Apple":
    y= Fruit_Dict["Apple"]
  elif x == "Orange":
    y= Fruit_Dict["Orange"]
  elif x == "Peach":
    y=Fruit_Dict["Peach"]
  elif x == "Pear":
    y=Fruit_Dict["Pear"]
  elif x == "Blueberry":
    y=Fruit_Dict["Blueberry"]
  else:
    y= "Sorry, we do not have data on that fruit"
  return y
y=fruit_function(x)
print(y)