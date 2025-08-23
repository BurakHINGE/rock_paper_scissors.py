while True:
	import random

	can = 3

	puan = 0

	oyun = ["taş","kağıt","makas"]

	while can != 0:
		x = random.randint(0,2)
		BilgisayarHamlesi = oyun[x]
		hamle = input("Taş, kağıt, makas?\n")
		if BilgisayarHamlesi == hamle:
			print("Berabere")

		elif hamle == "taş":
			if BilgisayarHamlesi == "kağıt":
				can -= 1
				print(f"Kaybettiniz, {can} canınız kaldı!")

			else:
				puan += 10
				print(f"Kazandınız, toplamda {puan} puanınız var!")

		elif hamle == "kağıt":
			if BilgisayarHamlesi == "makas":
				can -= 1
				print(f"Kaybettiniz, {can} canınız kaldı!")

			else:
				puan += 10
				print(f"Kazandınız, toplamda {puan} puanınız var!")


		elif hamle == "makas":
			if BilgisayarHamlesi == "taş":
				can -= 1
				print(f"Kaybettiniz, {can} canınız kaldı!")

			else:
				puan += 10
				print(f"Kazandınız, toplamda {puan} puanınız var!")	

	print(f"Tebrikler, oyun sonu toplam {puan} puan kazandınız!")
