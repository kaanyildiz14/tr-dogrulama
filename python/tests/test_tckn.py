import pytest

from tr_dogrulama import tckn


def test_kurala_uymayan_numara_gecersizdir():
    assert tckn.gecerli_mi("12345678901") is False


def test_kurala_uyan_numara_gecerlidir():
    assert tckn.gecerli_mi("10000000146") is True


@pytest.mark.parametrize(
    "hatali_giris",
    [
        "",               # boş
        "123",            # çok kısa
        "100000001460",   # çok uzun
        "1000000014a",    # harf içeriyor
        "00000000000",    # 0 ile başlıyor
        None,             # metin değil
    ],
)
def test_hatali_girisler_gecersizdir(hatali_giris):
    assert tckn.gecerli_mi(hatali_giris) is False