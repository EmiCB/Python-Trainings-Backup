# Imports!!!
import math

# Simple addition function -- pairs with PythonTrainingDay2.1_2017
def add_numbers( num1, num2 ):
	total = num1 + num2
	return total

# Classes!!!
# "self" passes itslef into itself -- self is always defined -- this instance
class Math_Class( ):
	def __init__ ( self, num1, num2 ):
		self.num1 = num1
		self.num2 = num2
	def add ( self ):
		total = self.num1 + self.num2
		return total

# you can use a class anywhere!
my_math_class = Math_Class ( 9, 10 ) # substitute num1 and num2 params with numbers
result = my_math_class.add()
print ( result )

# ------- ROBOT CODE NOTES --------

# comand-based robot code
# subsystems - functions of robot
# commands - tell subsystems what to do
# controls tied to commands

