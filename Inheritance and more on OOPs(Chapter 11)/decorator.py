def greet(fx):
    def modified_fx(*args, **kwargs):
        print('Good morning')
        fx()
        print('Thanks for using this function.')
    return modified_fx

@greet
def hello():
    print("hello world")

# hello = greet(hello) # i.e. greet(hello) = modified_fx
hello() # hello is no longer the original function it now refers to modified_fx, hence python executes modified_fx()