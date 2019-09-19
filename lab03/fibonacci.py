def main():
    print("This Program will give the nth Fibonacci number when n is inputed")
    a,b = 1,1
    num=eval(input("Please input what Fibonacci number you want to be calculated: "))
    num_int=int(num-2)
    for i in range (num_int):
        a,b=b,a+b
    print(b)
main()        