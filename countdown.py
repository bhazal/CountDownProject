import datetime
import time



def countdown():
    year = int(input("Hedef yılı girin: "))
    month = int(input("Hedef ay girin: "))

    while month not in range(1, 13):
        print("1'den 12'ye kadar bir sayı girin")
        month = int(input("Hedef ay girin: "))

    day = int(input("Hedef gün girin: "))

    while day not in range(1, 32):
        print("1'den 31'e kadar bir sayı girin")
        day = int(input("Geri sayılacak gün girin: "))

    

    time = datetime.datetime(year , month , day) - datetime.datetime.now()

    

    print(f"{time.days} gün kaldı")


countdown()



