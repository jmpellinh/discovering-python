def sum (num1, num2):
    result = num1 + num2
    return result
def main ():
    val1 = 3
    val2 = 4
    total = sum(val1, val2)
    print (total)
main ()

def get_name():
    name = input ("Name? ")
    return name
def main ():
    some_name = get_name ()
    print (some_name)
main ()

def is_even ():
    num =int(input("Input your num: "))
    if num % 2 == 0:
        return True
    else:
        return False
def main ():
    result = is_even ()
    print (result)
main ()
import math
print (math.pi)
