class Person:
  def __init__(self, name, age, address):
    self.name = name
    self.age = age
    self.address = address
class Student(Person): 
   def __init__(self, name, age, address, grade_level):
     Person.__init__(self, name, age, address)
     self.grade_level = grade_level
p1 = Student("Joe", 55, "45 Lees Creek Court Rego Park, NY 11374", 9)
print(p1.name)
print(p1.age)
print(p1.address)
print(p1.grade_level)