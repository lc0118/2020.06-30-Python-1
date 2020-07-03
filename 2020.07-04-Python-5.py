#Class, Object, 상속 복습
class Person:
  def __init__(self, name, age): 
    self.name = name
    self.age = age
  def say_hello(self, to_name):
    print("안녕! 나는 " + self.name + ", " + str(self.age) + "살이야, 너는 " + to_name + "지?")

class police(Person):
  def say_arrest(self, to_arrset):
    print("넌 체포됐다," + to_arrset)

for i in range(5): #심심해서 넣은 5번 반복
  wonie = Person("워니", 20) #이름, 나이
  wonie = police("워니", 20) #이름, 나이
  wonie.say_hello("철수") #이름
  wonie.say_arrest("철수") #이름