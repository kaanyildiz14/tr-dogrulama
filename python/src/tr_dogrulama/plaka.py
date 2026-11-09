import re

# Q, W, X ve Türkçe karakterler dışındaki büyük harfler
HARF = "[A-PR-VYZ]"

DESEN = re.compile(
    "([0-9]{2})"                    # il kodu
    "(?:"
    f"{HARF}{{1}}[0-9]{{4,5}}"      # 1 harf + 4-5 rakam
    f"|{HARF}{{2}}[0-9]{{3,4}}"     # 2 harf + 3-4 rakam
    f"|{HARF}{{3}}[0-9]{{2,3}}"     # 3 harf + 2-3 rakam
    ")"
)


def gecerli_mi(numara):
    if not isinstance(numara, str):
        return False

    temiz = numara.replace(" ", "").upper()

    eslesme = DESEN.fullmatch(temiz)
    if eslesme is None:
        return False

    il_kodu = int(eslesme.group(1))
    return 1 <= il_kodu <= 81