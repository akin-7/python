num2 = 45.99
try:
    num2 + num3
    import mathematics
    num2 = mathematics.flour(num2)
except ModuleNotFoundError:
    print("module does not exist, invent it")
except:
    print("an error was encountered")
