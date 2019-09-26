def main():
    n = int(input("Please enter a value for N:"))
    total = 0
    for i in range(0,n,2):
        total += ((1.0/(i+i+1))-(1.0)/(i+i+3))

    value = 4*total
    print(value)

main()    