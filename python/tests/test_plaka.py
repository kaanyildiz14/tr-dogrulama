import pytest

from tr_dogrulama import plaka


@pytest.mark.parametrize(
    "numara",
    [
        "35A1234",
        "35 A 12345",
        "06 AB 123",
        "34 AB 1234",
        "01 ABC 12",
        "81 ABC 123",
        "35 ab 123",      # küçük harfle yazım
    ],
)
def test_gecerli_plakalar(numara):
    assert plaka.gecerli_mi(numara) is True


@pytest.mark.parametrize(
    "hatali_giris",
    [
        "00 A 1234",      # il kodu çok küçük
        "82 A 1234",      # il kodu çok büyük
        "35 A 123",       # 1 harfte rakam eksik
        "35 AB 12",       # 2 harfte rakam eksik
        "35 ABC 1",       # 3 harfte rakam eksik
        "35 ABCD 12",     # fazla harf
        "35 Q 1234",      # Q kullanılmaz
        "35 Ç 1234",      # Türkçe karakter kullanılmaz
        "",               # boş
        None,             # metin değil
    ],
)
def test_hatali_girisler_gecersizdir(hatali_giris):
    assert plaka.gecerli_mi(hatali_giris) is False



@pytest.mark.parametrize(
    "girdi, beklenen",
    [
        ("35ab123", "35 AB 123"),
        ("35A1234", "35 A 1234"),
        ("01 ABC 12", "01 ABC 12"),
        ("81abc123", "81 ABC 123"),
    ],
)
def test_bicimlendir_parcalari_ayirir(girdi, beklenen):
    assert plaka.bicimlendir(girdi) == beklenen


@pytest.mark.parametrize("hatali_giris", ["00 A 1234", "", None])
def test_gecersiz_plaka_bicimlendirilemez(hatali_giris):
    assert plaka.bicimlendir(hatali_giris) is None