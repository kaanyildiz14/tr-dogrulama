import pytest

from tr_dogrulama import telefon


@pytest.mark.parametrize(
    "numara",
    [
        "05000000000",
        "5000000000",
        "+905000000000",
        "905000000000",
        "0500 000 00 00",
        "(0500) 000-00-00",
    ],
)
def test_gecerli_cep_telefonlari(numara):
    assert telefon.gecerli_mi(numara) is True


@pytest.mark.parametrize(
    "hatali_giris",
    [
        "02320000000",     # sabit hat
        "0500000000",      # eksik hane
        "050000000000",    # fazla hane
        "0500000000a",     # harf içeriyor
        "+15000000000",    # başka ülke kodu
        "",                # boş
        None,              # metin değil
    ],
)
def test_hatali_girisler_gecersizdir(hatali_giris):
    assert telefon.gecerli_mi(hatali_giris) is False



@pytest.mark.parametrize(
    "numara",
    [
        "05001112233",
        "5001112233",
        "+905001112233",
        "(0500) 111-22-33",
    ],
)
def test_bicimlendir_tek_tip_yazim_uretir(numara):
    assert telefon.bicimlendir(numara) == "0500 111 22 33"


@pytest.mark.parametrize("hatali_giris", ["02320000000", "", None])
def test_gecersiz_numara_bicimlendirilemez(hatali_giris):
    assert telefon.bicimlendir(hatali_giris) is None