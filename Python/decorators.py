#decoraters take another funciton and modify it.
#here the wrapper function takes the announce function and modifies its output.
def announce(f):
    def wrapper():
        print("About to run a function...")
        f()
        print("Done with the fucntion.")
    return wrapper

#here we have a function called hello and we are wrapping it within announce decorater
#using @.
@announce
def hello():
    print("hello, world!")

hello()
