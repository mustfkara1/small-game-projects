import random
import time

class SayisalLoto():
    __baslik="Sayısal Loto Kolonu Dolduran Program"

    def __init__(self):
        self.giris()

    def kolonSayisiBelirleme(self):
        while True:
            try:
                kolonSayisi = int(input("Kaç tane kolon üretelim? : "))
                return kolonSayisi
            except:
                print("Bir tam sayı girilmedi. Tekrar deneyin...")

    def giris(self):
        print("*"*len(self.__baslik),self.__baslik,"*"*len(self.__baslik),sep="\n",end="\n")

        while True:
            istek = input("Programdan çıkmak için 1'e devam etmek için herhangi bir tuşa basınız...")

            if istek == "1":
                print("Program Kapatılıyor...")
                time.sleep(1)
                break

            sayi = self.kolonSayisiBelirleme()#sayi tuple cinsinden olur.

            kolon = []
            kolonlar = []
            sayac = 0

            while sayac < sayi:
                for s in range(0,6):
                    numara = random.randint(1,50)
                    while numara in kolon:
                        numara = random.randint(1,50)
                    kolon.append(numara)
                    kolon.sort()

                if kolon not in kolonlar:
                    kolonlar.append(kolon)
                    sayac += 1
                    print("{}. kolon = {}".format(sayac,kolon))
                else:
                    kolon=[]
                
if __name__ == "__main__":
    sl = SayisalLoto()