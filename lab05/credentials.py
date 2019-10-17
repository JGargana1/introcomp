def main():
    first = input("Enter your first name: ")
    last = input ("Enter your last name: ")

    uname = first + "." + last

    while True:
        passwd = input("Create a new password: ")
        if len(passwd) < 8:
            print("Fool of a Took! That password is feeble!")
            passwd = input("Create a new password: ")
        else:
            print("The force is strong in this one...")
            print("Account configured. Your new email adress is",
                  uname + "@marist.edu")

main()