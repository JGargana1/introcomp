def main():
    animal = "bear"
    guess = ""
    while guess != animal:
        print("I am thinking of an animal, can you guess it?")
        guess = input("What animal am I thinking of: ")
        x = x.lower(guess)
        if x == animal:
            print("Congratulations, you guessed correctly!")
            break
        elif guess == "quit":
            break
        else:
           print("Wrong, guess again.")
        
            

main()