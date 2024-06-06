from pakiet.bankomat import Bankomat


class ProBankomat(Bankomat):

    def zakup_biletu(self):
        print("zakupiono bilet")

    def sprawdz_saldo(self):
        print(f"aktualne saldo: {self.saldo} EUR")
        return self.saldo