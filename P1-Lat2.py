ind = int(input("Nilai Bahasa Indonesia :"))
ipa = int(input("Nilai IPA :"))
mtk = int(input("Nilai Matematika :"))


if(ind < 0 or ind > 100):
    print("Maaf input yang ada tidak valid")
elif(ipa < 0 or ipa > 100):
    print("Maaf input yang ada tidak valid")
elif(mtk < 0 or mtk > 100):
    print("Maaf input yang ada tidak valid")
    
elif(ind > 60 and ipa > 60 and mtk > 70):
    print("Status kelulusan : LULUS")
else:
    print("Status kelulusan : TIDAK LULUS")
