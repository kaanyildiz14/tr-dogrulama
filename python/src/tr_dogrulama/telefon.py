import re


def _on_haneye_indir(numara):
    """Geçerli cep numarasını 10 haneye indirir (5001112233), geçersizse None döner."""
    if not isinstance(numara, str):
        return None

    # Boşluk, parantez ve tireleri sil
    temiz = re.sub(r"[ ()\-]", "", numara)

    # Başındaki ülke kodunu ya da sıfırı at
    if temiz.startswith("+90"):
        temiz = temiz[3:]
    elif temiz.startswith("90") and len(temiz) == 12:
        temiz = temiz[2:]
    elif temiz.startswith("0"):
        temiz = temiz[1:]

    # Geriye 5 ile başlayan 10 hane kalmalı
    if re.fullmatch(r"5[0-9]{9}", temiz):
        return temiz
    return None


def gecerli_mi(numara):
    return _on_haneye_indir(numara) is not None


def bicimlendir(numara):
    on_hane = _on_haneye_indir(numara)
    if on_hane is None:
        return None
    return f"0{on_hane[:3]} {on_hane[3:6]} {on_hane[6:8]} {on_hane[8:]}"