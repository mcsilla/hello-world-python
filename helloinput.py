def get_hello_message():
  name = input("What's your name?\n")
  if name == "":
    return "Hello, World!"
  else:
    return "Hello, " + name + "!"


def say_hello(message):
  print(message)


say_hello(get_hello_message())
