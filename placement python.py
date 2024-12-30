def add(a,b):
  return a+b
def sub(a,b):
  return a-b
def mul(a,b):
  return a*b
def div(a,b):
  if b==0:
    return "error! cannot divide by zero"
  return a/b
def cal():
  print("select operation")
  print("1.Addition:")
  print("2,Subtraction:")
  print("3.Multiplication:")
  print("4.Division:")
while True:
  choice=input("Enter choice(1/2/3/4):")
  if choice in('1','2','3','4'):
    try:
      n1=float(input("Enter the first number:"))
      n2=float(input("Enter the second number:"))
    except ValueError:
      print("Invalid input")
      continue
  if choice=='1':
    print(f"Result:{n1}+{n2}={add(n1,n2)}")
  elif choice=='2':
    print(f"Result:{n1}-{n2}={sub(n1,n2)}")
  elif choice=='3':
    print(f"Result:{n1}*{n2}={mul(n1,n2)}")
  elif choice=='4':
    print(f"Result:{n1}/{n2}={div(n1,n2)}")
  else:
    print("Invalid input")
cal()
