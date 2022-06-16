

def add(n1,n2):
    return n1 + n2
def sub(n1,n2):
    return n1 - n2



def caliculator():
  #operations = {"+": add(x, y), "-": sub(x, y), "*": multi(x, y), "/": div(x, y)}

  x = int(input("What is you first number: "))
  op=input("what operation you want to perform '+,-,*,/' : ")
  y = int(input("Enter your secdef add(n1,n2):
  return n1 + n2

def sub(n1,n2):
  return n1 - n2
ond number: "))
  operations = {"+": add(x, y), "-": sub(x, y), "*": multi(x, y), "/": div(x, y)}

  result= operations[op]
  print(result)
  again()
caliculator()
