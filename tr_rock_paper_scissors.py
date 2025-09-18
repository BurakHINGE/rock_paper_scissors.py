import random

while True:  
    basla = input("\nTaş Kağıt Makas oynamak için ENTER'a basın (çıkmak için q): ").lower()
    if basla == "q":
        print("Çıkış yapıldı. Görüşürüz!")
        break 
    
    can = 3
    puan = 0
    oyun = ["taş", "kağıt", "makas"]

    while can != 0:
        hamle = input("Taş, kağıt, makas? ").lower()
        
        if hamle not in oyun:
            print("Geçersiz hamle, tekrar deneyin!")
            continue

        BilgisayarHamlesi = random.choice(oyun)
        print(f"Bilgisayar seçti: {BilgisayarHamlesi}")

        if BilgisayarHamlesi == hamle:
            print("Berabere!")

        elif (hamle == "taş" and BilgisayarHamlesi == "makas") or \
             (hamle == "kağıt" and BilgisayarHamlesi == "taş") or \
             (hamle == "makas" and BilgisayarHamlesi == "kağıt"):
            puan += 10
            print(f"Kazandınız! Toplam puanınız: {puan}")

        else:
            can -= 1
            print(f"Kaybettiniz! Kalan canınız: {can}")

    print(f"Tebrikler, oyun bitti! Toplam {puan} puan kazandınız!")
