from pakiet.bankomat import Bankomat

print("witam w programie")

bankomat1 = Bankomat()
bankomat1.sprawdz_saldo()
bankomat1.wplata(1000)
bankomat1.sprawdz_saldo()
bankomat1.wyplata(500)
bankomat1.sprawdz_saldo()