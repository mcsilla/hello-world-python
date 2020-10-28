def get_user_name():
  name = input("What's your name?\n")
  return name.capitalize()
  

def get_hello_message(name):
  if name == "":
    return "Hello, World!"
  else:
    return "Hello, " + name + "!"


def say_hello(message):
  print(message)


say_hello(get_hello_message(get_user_name()))