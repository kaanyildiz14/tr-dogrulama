def gecerli_mi(numara):
    # Hesaplamadan önce girişin biçimini kontrol et
    if not isinstance(numara, str):
        return False
    if len(numara) != 10:
        return False
    if not (numara.isascii() and numara.isdigit()):
        return False

    haneler = [int(h) for h in numara]
    toplam = 0

    for sira, hane in enumerate(haneler[:9]):
        kalan = 9 - sira
        ara = (hane + kalan) % 10
        deger = (ara * 2**kalan) % 9
        if ara != 0 and deger == 0:
            deger = 9
        toplam += deger

    beklenen_son_hane = (10 - toplam % 10) % 10
    return haneler[9] == beklenen_son_hane