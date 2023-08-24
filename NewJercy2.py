import math as m
import Ohio as O
O.Name.Input()
Loop = True
while Loop == True:
    choose = str(input("คุณต้องการเลือก ห.ร.ม หรือ ค.ร.น\nกด 1 เพื่อคำนวณค่าตัวหารร่วมมากของจำนวนเต็มดังกล่าว\nกด 2 เพื่อคำนวณค่าตัวคูณร่วมน้อยของจำนวนเต็มดังกล่าว\nคุณต้องการคำนวณสิ่งไหน : "))
    Number1 = int(input("ตัวเลขตัวที่ 1 : "))
    Number2 = int(input("ตัวเลขตัวที่ 2 : "))
    if choose == "1":
        print("คุณเลือก ห.ร.ม")
        if Number1 > 0 and Number2 > 0:
            print("ห.ร.ม คือ {}".format(m.gcd(Number1,Number2)))
    elif choose == "2":
        print("คุณเลือก ค.ร.น")
        if Number1 > 0 and Number2 > 0:
            print("ค.ร.น คือ {}".format(m.lcm(Number1,Number2)))
    else:
        print("ไม่สามารถระบุความต้องการได้")
    ways = str(input("คุณต้องการคำนวณอีกครั้งหรือไม่ 1 = ต้องการ 2 = ไม่ต้องการ : "))
    if ways == "1":
        Loop = True
    else:
        if ways == "2":
            Loop = False