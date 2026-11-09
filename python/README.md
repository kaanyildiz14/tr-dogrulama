# tr-dogrulama

Türkiye'ye özgü verileri doğrulayan ve biçimlendiren,bağımlılıksız Python kütüphanesi,

## Kurulum

```bash
pip install tr-dogrulama
````

## Kullanım

```python
from tr_dogrulama import iban, plaka, tckn, telefon, vkn

tcnk.gecerli_mi("10000000146")            # True
vkn.gecerli_mi("1234567890")              # True
iban.gecerli_mi("TR330006100519786457841326")    # True

telefon.bicimlendir("+905001112233")     # "0500 111 22 33"
iban.bicimlendir("tr330006100519786457841326")
# "TR33 0006 1005 1978 6457 8413 26"
plaka.bicimlendir("35ab123")             # "35 AB 123"
```

Geçersiz girişlerde `gecerli_mi` `False`, `bicimlendir` `None` döner.

Doğrulama yalnızca numaranın biçimini ve kontrol hanelerini denetler. Numaranın gerçek bir kişiye, şirkete, hesaba ya da araca ait olduğunu göstermez.