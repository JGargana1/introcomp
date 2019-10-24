def show_intro():
    print("Welcome to the Arithmetic Engine!")
    print("=================================\n")
    print("Valid commands are 'add', 'mult', 'sub', 'div', and 'quit'./n")

def show_outro():
    print("\nThank you for using the Arithmetic Engine...")
    print("\nPlease come back again soon!")

def do_loop():
    while True:
        cmd = input("What computation do you want to perform?: ").lower()
        if cmd == "quit":
            break

        if not (cmd == "add" or cmd == "sub" or cmd == "mult" or cmd == "div"):
            print("This is not a valid Command.")
            continue

        num1 = int(input("Enter the first numnber: "))
        num2 = int(input("Enter the second number: "))
    
        if cmd == "add":
            result = num1 + num2
        elif cmd == "sub":
            result = num1 - num2
        elif cmd == "mult":
            result = num1 * num2
        elif cmd == "div":
            try:
                result = num1 / num2
            except:
                print("Unable to divide by zero!") 

        print ("The result is :", result, "\n")

def main():
    show_intro()
    do_loop()
    show_outro()

main()
                                