from pakiet.bankomat import Bankomat
from pakiet.probankomat import ProBankomat

print("witam w programie")

# bankomat1 = Bankomat()
# bankomat1.sprawdz_saldo()
# bankomat1.wplata(1000)
# bankomat1.sprawdz_saldo()
# bankomat1.wyplata(500)
# bankomat1.sprawdz_saldo()

def multi(a, b):
    try:
        return a * b
    except (TypeError, ValueError):
        return 0

def multi2(a, b):
    try:
        return a * b
    except Exception as e:
        return(e)

def multi3(a, b):
    try:
        suma = a * b
    except TypeError:
        return 0
    except ValueError:
        return 1
    else:
        return a * b
    finally:
        print("dzialanie zostalo zakonczone")

#
# print(multi(5,5))
# print(multi("5", "tomek"))
# print(multi2("5", "tomek"))
# print(multi3(5, 5))

bankomat2 = ProBankomat()
bankomat2.sprawdz_saldo()
bankomat2.wplata(1000)
bankomat2.sprawdz_saldo()
bankomat2.zakup_biletu()
