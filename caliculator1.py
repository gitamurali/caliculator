

def add(n1,n2):
    return n1 + n2
def sub(n1,n2):
    return n1 - n2

def multi(n1,n2):
  return n1 * n2

def div(n1,n2):
  return n1 / n2
def again():
  cal = input("Do you want to continue y or n : ")
  if cal=="y":
      caliculator()
  elif cal=="n":
      print("good bye!")

def caliculator():
  #operations = {"+": add(x, y), "-": sub(x, y), "*": multi(x, y), "/": div(x, y)}

  x = int(input("What is you first number: "))
  op=input("what operation you want to perform '+,-,*,/' : ")
  y = int(input("Enter your secdef add(n1,n2):
  operations = {"+": add(x, y), "-": sub(x, y), "*": multi(x, y), "/": div(x, y)}

  result= operations[op]
  print(result)
  again()
caliculator()
