def main():
    animal = "bear"
    guess = ""
    while guess != animal:
        print("I am thinking of an animal, can you guess it?")
        guess = input("What animal am I thinking of: ")
        x = (guess)
        if x == animal:
            print("Congratulations, you guessed correctly!")
            break
        elif guess != animal:
            print("Wrong, guess again.")

main()