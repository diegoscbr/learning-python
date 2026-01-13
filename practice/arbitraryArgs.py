'''
Docstring for arbitraryArgs

*args  = allows you to pass multile non-keyword arguments
**kwargs = allows you to pass multiple keyword arguments
    * unpacking operator

'''

def add(a, b):
    return a + b

def arbitraryAdd(*args):
    total = 0
    #*args stored as touples
    print(type(args))
    for arg in args:
        total += arg
    return total


print(arbitraryAdd(1,3,4,5,6,7))



# **kwargs example alows you to pass multiple keyword segments
def printAddr(**kwargs):
    '''
    Docstring for printAddr
    
    :param kwargs: keyword segments for addrs
    Usage: printAddr(Street =, State = , City=, )
    '''
    #kwargs stored as a map
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key}: {value}")

printAddr(street="3175 Cauby Street", city="San Diego", state="CA")

#you can also add *args and **kwargs 
def shippingLabel(*args, **kwargs):
    print("NAME: ", end = " ")
    for arg in args:
        print(arg, end = " ")
    print("")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

    

shippingLabel("Dr.", "Diego", "Escobar", 
              street="123 Sesame St", city="New York", state = "NY")


name = 'Jackson' 

