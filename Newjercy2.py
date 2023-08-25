Choose = str(input("Which method do you want to do? 1:GCD 2:LCM : "))
Number1 = int(input("Num1 : "))
Number2 = int(input("NUm2 : "))
if Choose == "1":
    if Number1 > Number2:
        small = Number2
    else:
        small = Number1
    for i in range(1,small + 1):
        if((Number1 % i == 0) and (Number2 % i == 0)):
            gcd = i
    print("The GCD is {}".format(gcd))
if Choose == "2":
    if Number1 > Number2 :
        greater = Number1
    else:
        greater = Number2
    while(True):
        if((greater % Number1 == 0) and (greater % Number2 == 0)):
            lcm = greater
            break
        greater += 1
    print("The LCM is {}".format(lcm))       