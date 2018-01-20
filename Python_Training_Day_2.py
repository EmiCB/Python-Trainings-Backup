# While loops
i = 0
while i < 10:
    print (i)
    i += 1
    
# For loops
for i in range(10):
    print(i)
    
# For loops with strings
all_things = ['cat', 'dog','zombie']
num_things =len(all_things)

for i in range(num_things):
    print(all_things[i])

#Better way for the all things thing
for thing in all_things:
    print(thing)
    
#Imports
import math
print(math.pi)
print(math.sqrt(16))