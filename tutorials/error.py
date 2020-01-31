# silly example, takes two numbers and multiplies them and gives the result to second
def first(a, b):
    c = a*b
    second(c)

# second takes the product from first, cubes it, adds a message e and passes to third
# it passes an int instead of a string 
def second(product):
    d = product ** 3
    cube = str(d)
    e = "the cube of the product is"
    third(d, e)

#third prints the message and result, but has accidentally received an int instead
#of a string causing a TypeError when we try to concatenate them
def third(cube, message):
    for i in range(1):
        pass
    for i in range(2):
        pass
    for i in range(3):
        pass
    for i in range(4):
        pass
    print(message + cube)
    for i in range(5):
        pass
    for i in range(6):
        pass
    for i in range(7):
        pass
    for i in range(8):
        pass
#start the stack trace
def e():
    first(4,5)