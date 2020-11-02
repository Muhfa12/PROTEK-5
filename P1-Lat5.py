kodeKaryawan = int(input("Masukkan kode karyawan :"))
namaKaryawan = input("Masukkan nama karyawan :")
golongan = input("Masukkan golongan :")
status = input("Masukan status (1:menikah, 2:blm):")
if(status == '1'):
    jumlahAnak = int(input("Masukan Jumlah Anak: "))
    tunjanganMenikah = 10 / 100
    tunjanganAnak = 5 / 100 * jumlahAnak
    statusMenikah = "Sudah Menikah"
else:
    jumlahAnak = 0
    tunjanganMenikah = 0
    tunjanganAnak = 0
    statusMenikah = "Belum Menikah"

if(golongan == 'A'):
    GajiPokok = 10000000
    Potongan = 2.5
    JumlahTunjanganMenikah = 10000000 * tunjanganMenikah
    JumlahTunjanganAnak = 10000000 * tunjanganAnak
    GajiKotor = 10000000 - JumlahTunjanganMenikah + JumlahTunjanganAnak
    JumlahPotongan = 2.5 / 100 * GajiKotor
    GajiBersih = GajiKotor - JumlahPotongan
elif(golongan == 'B'):
    GajiPokok = 8500000
    Potongan = 2.0
    JumlahTunjanganMenikah = 8500000 * tunjanganMenikah
    JumlahTunjanganAnak = 8500000 * tunjanganAnak
    GajiKotor = 8500000 - JumlahTunjanganMenikah + JumlahTunjanganAnak
    JumlahPotongan = 2. / 100 * GajiKotor
    GajiBersih = GajiKotor - JumlahPotongan
elif(golongan == 'C'):
    GajiPokok = 7000000
    Potongan = 1.5
    JumlahTunjanganMenikah = 7000000 * tunjanganMenikah
    JumlahTunjanganAnak = 7000000 * tunjanganAnak
    GajiKotor = 7000000 - JumlahTunjanganMenikah + JumlahTunjanganAnak
    JumlahPotongan = 1.5 / 100 * GajiKotor
    GajiBersih = GajiKotor - JumlahPotongan
elif(golongan == 'D'):
    GajiPokok = 5500000
    Potongan = 1.0
    JumlahTunjanganMenikah = 5500000 * tunjanganMenikah
    JumlahTunjanganAnak = 5500000 * tunjanganAnak
    GajiKotor = 5500000 - JumlahTunjanganMenikah + JumlahTunjanganAnak
    JumlahPotongan = 1.0 / 100 * GajiKotor
    GajiBersih = GajiKotor - JumlahPotongan

print("=========================================")

print("STRUK RINCIAN GAJI KARYAWAN")

print("-----------------------------------------")

print("Nama Karyawan :" + namaKaryawan + "(Kode Karyawan :" + str(kodeKaryawan))

print("Golongan :" + golongan)
print("Status :" + statusMenikah)
print("Jumlah anak :" + str(jumlahAnak))

print("-----------------------------------------")
    
print("Gaji Pokok : Rp" + str(GajiPokok))
print("Tunjangan Menikah : Rp" + str(JumlahTunjanganMenikah))
print("Tunjangan Anak : Rp" + str(JumlahTunjanganAnak))

print('-----------------------------------------")

print("Gaji Kotor : Rp" + str(GajiKotor))
      
print("Potongan (" + str(Potongan) + "%): Rp" + str(JumlahPotongan))

print("-----------------------------------------')

print("Gaji Bersih : Rp" + str(GajiBersih))
