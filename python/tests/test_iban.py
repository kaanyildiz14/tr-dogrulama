import pytest

from tr_dogrulama import iban

GECERLI = "TR330006100519786457841326"


@pytest.mark.parametrize(
    "numara",
    [
        GECERLI,
        "TR33 0006 1005 1978 6457 8413 26",   # boşluklu yazım
        GECERLI.lower(),                      # küçük harfle yazım
    ],
)
def test_gecerli_ibanlar(numara):
    assert iban.gecerli_mi(numara) is True


@pytest.mark.parametrize(
    "hatali_giris",
    [
        "TR330006100519786457841327",   # son hane yanlış
        "TR000006100519786457841326",   # kontrol hanesi yanlış
        "DE89370400440532013000",       # Türkiye IBAN'ı değil
        "TR33000610051978645784132",    # eksik karakter
        "TR33000610051978645784132A",   # harf içeriyor
        "",                             # boş
        None,                           # metin değil
    ],
)
def test_hatali_girisler_gecersizdir(hatali_giris):
    assert iban.gecerli_mi(hatali_giris) is False



@pytest.mark.parametrize(
    "numara",
    [
        GECERLI,
        GECERLI.lower(),
        "TR33 0006 1005 1978 6457 8413 26",
    ],
)
def test_bicimlendir_dortlu_gruplar_uretir(numara):
    assert iban.bicimlendir(numara) == "TR33 0006 1005 1978 6457 8413 26"


@pytest.mark.parametrize(
    "hatali_giris",
    ["TR330006100519786457841327", "", None],
)
def test_gecersiz_iban_bicimlendirilemez(hatali_giris):
    assert iban.bicimlendir(hatali_giris) is None