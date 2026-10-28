#Decorator = A function thatextends the behaviour of another function | w/o modifying the base function | Pass the base function as an argument to the decorator 

    # @add sprinklers 
    # get_ice_cream("vannila")
def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("you add sprinkler")
        func(*args , **kwargs)
    return wrapper
    
def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("you add fudge")
        func(*args,**kwargs)
    return wrapper
    
@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print("Here is your {flavor} icecream 🍨🍦")

get_ice_cream("strawberry")