def foo():
    print("Function foo() from module.py")


if __name__ == "__main__":
    print("module.py is being run directly")
else:
    print("module.py has been imported")
