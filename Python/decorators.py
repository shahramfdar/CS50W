def announce(f):
    def wrapper():
        print("About to run a function...")
        f()
        print("Done with the fucntion.")
    return wrapper
@announce
def hello():
    print("hello, world!")

hello()
