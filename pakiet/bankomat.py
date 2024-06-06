class Bankomat:
    def __init__(self, poczatkowe_saldo=0):
        self.saldo = poczatkowe_saldo

    def wplata(self,kwota):
        if kwota > 0:
            self.saldo += kwota
            print(f"wplacono {kwota} PLN. Aktualne saldo: {self.saldo} PLN")
        else:
            print("kwota wplaty musi byc wieksza od zera")

    def wyplata(self, kwota):
        if kwota > 0:
            if self.saldo >= kwota:
                self.saldo = kwota
                print(f"Wyplacono {kwota} PLN. aktualne saldo: {self.saldo} PLN")
            else:
                print("nie wystarczajace srodki")
        else:
            print("kwota wyplaty musi byc wieksza od zera")

    def sprawdz_saldo(self):
        print(f"aktualne saldo: {self.saldo} PLN")
        return self.saldo