ind = int(input("Nilai Bahasa Indonesia :"))
if(ind >= 0 and ind <= 100):

    ipa = int(input("Nilai IPA:"))
if(ipa >= 0 and ipa <= 100):
    
    mtk = int(input("Nilai Matematika :"))
if(mtk >= 0 and mtk <= 100):
    
    print("Status Kelulusan :")
    
if(ind>60 and ipa>60 and mtk>70):
    print('LULUS')
else:
    print("TIDAK LULUS")
