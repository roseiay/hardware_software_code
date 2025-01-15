def greeting(name):
    print("Hi {}!".format(name.capitalize()))
    print("Welcome to my conversation program!!!")
    print("Glad to have you in Hardware & Software!!!")

def main():
    greeting(input("What is your name? "))
    greeting(input("What is your name? "))

if __name__ == "__main__":
    main()
