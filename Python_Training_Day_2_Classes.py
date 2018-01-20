 # Class
 def __init__(self, num1, num2):
		self.num1 = num1
		self.num2 = num2
		
	def add(self):
		total = self.num1 + self.num2
		return total
	
# Calling class
my_fancy_math = Fancy_Math (15, 85)
result = my_fancy_math.add()
print(result)