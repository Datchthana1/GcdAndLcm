import math as m
import Ohio as O
O.Name.Input()
Loop = True
while Loop == True:
    choose = str(input("GCD or LCM\n 1:GCD\n 2:LCM\nWhich do you want to do?\n : "))
    Number1 = int(input("Number1 : "))
    Number2 = int(input("Number2 : "))
    if choose == "1":
        print("You choose GCD")
        if Number1 > 0 and Number2 > 0:
            print(f"GCD is {m.gcd(Number1,Number2)}")
    elif choose == "2":
        print("You choose LCM")
        if Number1 > 0 and Number2 > 0:
            print(f"LCM is {m.lcm(Number1,Number2)}")
    else:
        print("Cannot define??!")
    ways = str(input("Do you want to repeat? 1 = Yes 2 = No : "))
    if ways == "1":
        Loop = True
    else:
        if ways == "2":
            Loop = False
