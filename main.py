class BankHisob:
    def __init__(self, egasi, balans):
        self.egasi = egasi
        self.__balans = balans

    def pul_qosh(self, summa):
        self.__balans += summa

    def pul_yech(self, summa):
        self.__balans -= summa

    def info(self):
        print(f"Egasi: {self.egasi}")
        print(f"Balans: {self.__balans}")


b1 = BankHisob("Ali", 20)
b1.pul_qosh(20)
b1.info()

b1.pul_yech(10)
b1.info()
