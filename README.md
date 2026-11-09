# tr-dogrulama

[![Python](https://github.com/kaanyildiz14/tr-dogrulama/actions/workflows/python.yml/badge.svg)](https://github.com/kaanyildiz14/tr-dogrulama/actions/workflows/python.yml)
![Lisans](https://img.shields.io/badge/lisans-MIT-green)

Türkiye'ye özgü verileri doğrulayan ve biçimlendiren kütüphane.

| Veri | Doğrulama | Biçimlendirme |
|---|---|---|
| TC Kimlik No | Kontrol haneleri | |
| Vergi Kimlik No | Kontrol hanesi | |
| IBAN | ISO 7064 mod 97 | `TR33 0006 1005 ...` |
| Cep telefonu | Biçim | `0500 111 22 33` |
| Plaka | İl kodu ve biçim | `35 AB 123` |

Python sürümünün kurulumu ve kullanımı için [python/README.md](python/README.md) dosyasına bakın.

Doğrulama yalnızca numaranın biçimini ve kontrol hanelerini denetler. Numaranın gerçek bir kişiye, şirkete, hesaba ya da araca ait olduğunu göstermez.

## Geliştirme

```bash
cd python
python3 -m venv .venv
source .venv/bin/activate
pip install -e . pytest
pytest
```

## Lisans

[MIT](LICENSE)
