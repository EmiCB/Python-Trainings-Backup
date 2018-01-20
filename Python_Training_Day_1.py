# hopping with return

# names don't conflict outside vs inside a function
# varriables will be different inside vs outside

def add_one(num):
    new_num = num + 1
    return new_num

new_num = add_one(32)
print(new_num)

# Come up with a new script with a new function