'''
Allow us to modify the behaviour of a function or class. 
Allow us to wrap another function in another function in order to extend the behaviour of the wrapped function, 
    without permanently modifying it.
'''

def func1(func2):
    def func3():
        print("func3 function executing..")
        func2()
        print("func3 function executed")
    return func3

@func1
def func4():
    print("func4 function executed")

# ====== We can use this instead of using @decorator, works the same ==========
# func4 = func1(func4)

func4()




