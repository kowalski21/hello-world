from time import sleep

def check(y):
  if y<2:
    print("The door is locked")

def passer(name="user"):
  print("Hello {}!!!".format(name))
  print("database has been completed")

def hello(name="Kwame"):
  print("Hello "+ name)

  def divide(x,y):
    return y/x

  if __name__=="__main__":
    passer("Kofi")
    print("The application is working well")
