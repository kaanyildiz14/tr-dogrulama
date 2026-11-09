import pytest

from tr_dogrulama import vkn


@pytest.mark.parametrize("numara", ["1234567890", "0000000001"])
def test_kurala_uyan_numaralar_gecerlidir(numara):
    assert vkn.gecerli_mi(numara) is True


@pytest.mark.parametrize(
    "hatali_giris",
    [
        "1234567891",     # kontrol hanesi yanlış
        "0000000000",     # kontrol hanesi yanlış
        "",               # boş
        "123",            # çok kısa
        "12345678901",    # çok uzun
        "123456789a",     # harf içeriyor
        None,             # metin değil
    ],
)
def test_hatali_girisler_gecersizdir(hatali_giris):
    assert vkn.gecerli_mi(hatali_giris) is False