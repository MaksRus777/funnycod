class ManagedResource:
    def __enter__(self):
        print("Resource is being opened.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Resource is being closed.") 

with ManagedResource():
    print("I am using the managed resource!")