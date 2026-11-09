def gecerli_mi(numara):
    if not isinstance(numara, str):
        return False

    # 1. Boşlukları sil, harfleri büyüt
    temiz = numara.replace(" ", "").upper()

    # Biçim kontrolü: 26 karakter, TR ile başlıyor, gerisi rakam
    if len(temiz) != 26:
        return False
    if not temiz.startswith("TR"):
        return False
    rakamlar = temiz[2:]
    if not (rakamlar.isascii() and rakamlar.isdigit()):
        return False

    # 2. İlk 4 karakteri sona taşı
    yer_degismis = temiz[4:] + temiz[:4]

    # 3. Harfleri sayıya çevir (A=10, B=11 ... T=29, R=27)
    sayi_metni = "".join(str(int(karakter, 36)) for karakter in yer_degismis)

    # 4. 97'ye bölümünden kalan 1 olmalı
    return int(sayi_metni) % 97 == 1