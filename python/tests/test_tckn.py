from tr_dogrulama import tckn

def test_kurala_uymayan_numara_gecersizdir():
    assert tckn.gecerli_mi("12345678901") is False

def test_kurala_uyan_numara_gecerlidir():
    assert tckn.gecerli_mi("10000000146") is True