def plus_one(function):
    def wrapper(number):
        x = function(number)
        return x+1
    return wrapper

@plus_one
def just_number(x):
    return x

print(just_number(10))