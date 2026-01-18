run = 1
while run == 1 : 
    N1 = float(input("enter N1:"))
    N2 = float(input("enter N2:"))

    print("-,/,//,%,*,**,+")
    operator = input("enter operator:")

    if operator == "-" :
        calculation = N1 - N2
    elif operator == "/" :
        calculation = N1 / N2
    elif operator == "//" :
        calculation = N1 // N2
    elif operator == "%" :
        calculation = N1 % N2
    elif operator == "*" :
        calculation = N1 * N2
    elif operator == "**" :
        calculation = N1 ** N2
    elif operator == "+" :
        calculation = N1 + N2
    else :
        print("invalid operator is used ")
        continue

    print("calculation:", calculation)

    choice = input("enter 1 to continue,0 to stop:")
    run = int(choice)

#---------------------------------------------------------------------#
    # Positive / Negative / Zero
    if calculation > 0 :
        print("calculation is positive")
    elif calculation < 0 :
        print("calculation is negative")
    else :
        print("calculation is ZERO")

#---------------------------------------------------------------------#
    # Integer or Decimal
    if calculation == int(calculation):
        print("calculation is an integer")
        n = int(calculation)
    else:
        print("calculation is a decimal number")
        continue   # stop further integer-only checks

#---------------------------------------------------------------------#
    # Even / Odd
    if n % 2 == 0 :
        print("calculation is an even number")
    else :
        print("calculation is an odd number")

#---------------------------------------------------------------------#
    # Prime / Composite
    if n > 1 :
        count = 0
        for i in range(1, n+1) :
            if n % i == 0:
                count += 1
        if count == 2 :
            print("calculation is a prime number")
        else :
            print("calculation is a composite number")
    else :
        print("calculation is not prime or composite")

#---------------------------------------------------------------------#
    # Natural / Whole
    if n > 0 :
        print("calculation is a natural number")
    if n >= 0 :
        print("calculation is a whole number")

#---------------------------------------------------------------------#
    # Perfect Square
    if n >= 0 :
        if int(n**0.5)**2 == n :
            print("calculation is a perfect square")
        else :
            print("calculation is not a perfect square")

#---------------------------------------------------------------------#
    # Perfect Cube
    cube = round(n ** (1/3))
    if cube**3 == n :
        print("calculation is a perfect cube")
    else :
        print("calculation is not a perfect cube")

#---------------------------------------------------------------------#
    # Palindrome
    if n < 0 :
        print("calculation is not valid for palindrome number check")
    else :
        if str(n) == str(n)[::-1] :
            print("calculation is a palindrome number")
        else : 
            print("calculation is not a palindrome number")

#---------------------------------------------------------------------#           
    # Armstrong
    if n < 0 :
        print("calculation is not valid for armstrong number check")
    else :
        num_str = str(n)
        num_digits = len(num_str)
        sum_pow = sum(int(d)**num_digits for d in num_str)

        if sum_pow == n :
            print("calculation is an armstrong number")
        else :
            print("calculation is not an armstrong number")

#---------------------------------------------------------------------#
