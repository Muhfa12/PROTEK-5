print("Hai... nama saya Mr,Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silahkan tebak ya!!!")
tb = int(input("Tebakan Anda : "))
false = 0
while True:
    if(tb < 10):
        print("Hehehe... Bilangan tebakan anda terlalu kecil")
        tb = int(input("Tebakan Anda : "))
        false += 2
    elif(tb > 10):
        print("Hehehe... Bilangan tebakan anda terlalu besar")
        tb = int(input("Tebakan Anda : "))
        false += 2
    elif(tb == 10):
        print("yeee... Bilangan tebakan anda BENAR")
        score = 100 - false
        print("Score Anda :" + str(score))
        break
