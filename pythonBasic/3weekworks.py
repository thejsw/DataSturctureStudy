# -*- coding: utf-8 -*-
"""3weekWorks

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FybBcGAQsQrg8WdvRs_1gB6uhzcsXHUq
"""

def is_included (word, sentence):
  if word in sentence:
    return "yes"
  else:
    return "no"

print(is_included("love", "i love you"))
print(is_included("me", "i love you"))
print(is_included("you", "i love you"))

def do_sum():
  num = []
  for i in range(5):
    inp = input("Type the number: ")
    num.append(int(inp))

  sum = 0
  for i in num:
    sum += i
  
  print(sum)

if __name__ == '__main__' :
  do_sum()

phonebook = dict()

def insert(name, number):
  phonebook[name] = number
  
  
def delete(name):
  return phonebook.pop(name, -1)

def search(name):
  if name in phonebook:
    return phonebook[name] 

def scan():
  print(phonebook)

if __name__ == '__main__' :
  while 1:
    choice = input("Select the menu. 1:insert, 2:delete, 3:search, 4:scan, 5:quit : ")
    if choice == "1":
      name = input("Type your name: ")
      number = input("Type your number: ")
      insert(name, number)
    elif choice == "2":
      name = input("Type your name: ")
      delete(name)
    elif choice == "3":
      name = input("Type your name: ")
      number = search(name)
      print(number)
    elif choice == "4":
      scan()
    elif choice == "5":
      break
    else:
      print("Wrong number")

class Employee:
  counter = 0
  def __init__(self, name="NULL", salary=0):
    Employee.counter += 1
    self.__name = name
    self.__salary = salary
  def get_name(self):
    return self.__name
  def get_salary(self):
    return self.__salary
  def get_emp_cnt(self):
    return Employee.counter

if __name__ == '__main__' :
  Company = []
  data = {'Alcie':200, 'Bob':300, 'Mike':100}

  for key in data:
    emp = Employee(key, data[key])
    Company.append(emp)

  print("Total number of Employee: ", Company[0].get_emp_cnt())

  max_salary = 0
  max_name = ""
  for emp in Company:
    if int(emp.get_salary()) > max_salary:
      max_name = emp.get_name()
      max_salary = int(emp.get_salary())
  
  print("Max-salary employee: ", max_name, max_salary)

