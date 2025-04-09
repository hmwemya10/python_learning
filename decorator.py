def greet(fun):
    def wrapper(name):
        #before task calling sayName
        print('hi')
        fun(name)
        #after task calling sayName
        print('bye')
    return wrapper

    
@greet
def sayName(name):
    # print('hmmk')
    print(name)

sayName("mg mg")