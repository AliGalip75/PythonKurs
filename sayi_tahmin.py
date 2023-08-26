import random
sayi = random.randint(1,50)
hak = 5
sayac = 0
puan = 0
print("Sayi 1-50 araliginda olup tahmin hakkiniz 5'dir.")
while hak>0:
    hak -= 1
    sayac += 1
    tahmin = int(input("Tahmininizi girin: "))
    if tahmin == sayi:
        print(f"Tebrikler,{sayac}.denemede bildiniz.Puaniniz {100-puan}")
        break
    elif tahmin>sayi:
        puan += 20
        if hak != 0:
            print("Daha az.")
    else:
        puan += 20
        if hak != 0:
            print("Daha yüksek.")
    if hak == 0:
        print(f"Tahmin hakkiniz kalmadi.Tutulan sayi {sayi},puaniniz {100-puan} .")