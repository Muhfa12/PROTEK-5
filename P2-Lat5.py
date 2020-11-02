print("Hai... nama saya Mr,Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silahkan tebak ya!!!")
tb = int(input("Tebakan Anda : "))
while True:
    if(tb < 10):
        print("Hehehe... Bilangan tebakan anda terlalu kecil")
        tb = int(input("Tebakan Anda : "))
    elif(tb > 10):
        print("Hehehe... Bilangan tebakan anda terlalu besar")
        tb = int(input("Tebakan Anda : "))
    elif(tb == 10):
        print("yeee... Bilangan tebakan anda BENAR")
        break
