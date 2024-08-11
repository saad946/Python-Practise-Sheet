def my_function():
    print("Hello, World!")

my_function() 

print(__name__) # it will print "__main__" because this script is being run directly, not imported as a module. but if this script was imported as a module, __name__ would be the name of the module


if __name__ == "__main__":
    #if this code is executed by running this script directly, it will call the function
    print("This script is being run directly.")