import threading

def printit():
  threading.Timer(5.0, printit).start()
  print ("Hello, from EC2!")

printit()