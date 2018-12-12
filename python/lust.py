#!/usr/bin/env python

class LustObject(object):
  # executes the command
  def handle(self, arguments): pass
  def print_help(self): pass

class FactorialCommand(LustObject):
  def handle(self, arguments):
    try: argument = int(arguments[0])
    except (ValueError, IndexError):
      print("fact: could not read integer argument.")
      return

    if argument < 0:
      print("fact: argument has to be non-negative!")
      return

    print(self.__calculate_factorial(argument))

  def print_help(self):
    print(" fact <integer>")
    print("   Calculates the factorial of <integer>.")

  def __calculate_factorial(self, argument):
    # Hmmm...
    result = 1
    for i in range(1, argument+1):
      result *= i
    return result

class QuitCommand(LustObject):
  def handle(self, arguments = None):
    print("Bye!")
    exit()
  def print_help(self):
    print(" quit")
    print("   Quits.")

class HelpCommand(LustObject):
  def __init__(self, commands):
    self.commands = commands
  def handle(self, arguments = None):
    print("List of all commands")
    print("--------------------")
    for command in sorted(self.commands):
      self.commands[command].print_help()
  def print_help(self):
    print(" help")
    print("   Prints help for all commands.")


print("Hello! Welcome to the LARICS Universal Shell Terminal (LUST)!")
print("Enter 'help' for a list of commands. Press Ctrl-D or enter 'quit' to quit.")

# dictionary for storing all commands
commands = { }

commands["fact"] = FactorialCommand()
commands["quit"] = QuitCommand()
# help command needs a reference to the parent dictionary in order to call each
# command's print_help() function
commands["help"] = HelpCommand(commands)

# input from Python 3 is raw_input in Python 2
try: input = raw_input
except NameError: pass

while True:
  # read current line and try to extract command name
  try:
    cmd_line = input(">> ")
  except (EOFError):
    break
  arguments = cmd_line.split()
  try: cmd_name = arguments[0].lower()
  except IndexError: continue

  # look up the appropriate command in commands dictionary
  if cmd_name not in commands:
    print("lust: no such command '{}'.".format(cmd_name))
    continue
  else:
    # command found, pass its handler the rest of the read arguments
    commands[cmd_name].handle(arguments[1:])

print
commands["quit"].handle()
