import re


def gecerli_mi(numara):
    if not isinstance(numara, str):
        return False

    # 1. Boşluk, parantez ve tireleri sil
    temiz = re.sub(r"[ ()\-]", "", numara)

    # 2. Başındaki ülke kodunu ya da sıfırı at
    if temiz.startswith("+90"):
        temiz = temiz[3:]
    elif temiz.startswith("90") and len(temiz) == 12:
        temiz = temiz[2:]
    elif temiz.startswith("0"):
        temiz = temiz[1:]

    # 3. Geriye 5 ile başlayan 10 hane kalmalı
    return re.fullmatch(r"5[0-9]{9}", temiz) is not None