#ex 1
def main ():
    numbers ()
    print ("End of the program!")
def numbers ():
    for i in range (1,11):
        print (i)
main ()

#ex 2
def main ():
    greet ()
def greet ():
    name = input ("Name: ")
    print (f'Hello {name}!')
    print ("Nice to meet you!")
main ()

#ex 3
def main ():
    value = 5
    show_double (value)
def show_double (number):
    result = number * 2
    print (result)
main ()