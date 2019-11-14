from robotclass import Robotclass


def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
    
        vals = input ("Enter product ID and quanity you wish to buy: ").split(" ")
        if vals[0] == "quit": break

        name = int(vals[0])
        quantity = int(vals[1])

        if product_quantities[name] >=quantity:
            if cash >= product_prices[name]:
                product_quantities[name] * quantity
                cash -= product_prices[name] * quantity
                print("You purchased", quantity, product_names[name] + ".")
                print("You have $", "{0:.2f}".format(cash), "remaining.")
            else:
                print("Sorry, you cannot afford that product.")
        else:
            print("Sorry, we are sold out of", product_names[name])
main()                          