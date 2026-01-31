import random
import json

kullanici_adi = input("Kullanıcı adınızı giriniz: ")


try:
    with open("skorlar.json", "r") as file:
        veriler = json.load(file)
except FileNotFoundError:
    veriler = {}

if kullanici_adi not in veriler:
    veriler[kullanici_adi] = {"puan" : 0, "oyun_sayisi" : 0, "bota_karsi_kazanma" : 0, "bota_karsi_beraberlik" : 0, "bota_karsi_kaybetme" : 0}



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


    veriler[kullanici_adi]["puan"] += puan
    veriler[kullanici_adi]["oyun_sayisi"] += 1

    if puan > 30:
        veriler[kullanici_adi]["bota_karsi_kazanma"] += 1
    
    elif puan == 30:
        veriler[kullanici_adi]["bota_karsi_beraberlik"] += 1

    else:
        veriler[kullanici_adi]["bota_karsi_kaybetme"] += 1

    with open("skorlar.json", "w") as file:
        json.dump(veriler, file, indent=4)

    stats = veriler[kullanici_adi]

    print(f"{kullanici_adi} \nToplam Puan: {stats['puan']}"
      f"\nOynanan Oyun Sayısı: {stats['oyun_sayisi']}"
      f"\nBota karşı kazanma: {stats['bota_karsi_kazanma']}"
      f"\nBota karşı beraberlik: {stats['bota_karsi_beraberlik']}"
      f"\nBota karşı kaybetme: {stats['bota_karsi_kaybetme']}")
