ali_hesap = {
    "ad":"Ali Galip",
    "hesapNo":124356,
    "bakiye":2000,
    "ekHesap":3000
}
emine_hesap = {
    "ad":"Emine",
    "hesapNo":153221,
    "bakiye":2500,
    "ekHesap":1000
}
def para_cek(hesap_ad,miktar):
    print(f"Merhaba {hesap_ad['ad']}")
    kontrol = int(input("Kart sifrenizi giriniz:"))
    if kontrol == hesap_ad["hesapNo"]:
        if miktar<=hesap_ad["bakiye"]:
            print("Paranizi alabilirsiniz.")
            hesap_ad["bakiye"] = hesap_ad["bakiye"] - miktar
            print(f"Kalan bakiye:{hesap_ad['bakiye']}")
        else:
            toplam = hesap_ad["bakiye"] + hesap_ad["ekHesap"]
            if miktar<=toplam:
                ek_hesap_kulanimi = input("Ek hesap kullanilsin mi?(e/h)")
                if ek_hesap_kulanimi=="e":
                    print("Paranizi alabilirsiniz.")
                    hesap_ad['ekHesap'] = hesap_ad['ekHesap'] - (miktar - hesap_ad['bakiye'])
                    hesap_ad['bakiye'] = 0
                    print(f"Kalan bakiyeniz:{hesap_ad['bakiye']},ek hesapta kalan bakiyeniz:{hesap_ad['ekHesap']}.")
                else:
                    print(f"{hesap_ad['hesapNo']} no'lu hesabinizda {hesap_ad['bakiye']} tl,ek hesabinizda {hesap_ad['ekHesap']} tl bulunmaktadir.")
            else:
                print("Bakiyeniz yetersiz.")
    else:
        print("Yanlis sifre girdiniz.")

para_cek(ali_hesap,3000)



