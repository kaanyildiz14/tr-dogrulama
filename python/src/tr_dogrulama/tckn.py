def gecerli_mi(numara):
    haneler = [int(h) for h in numara]

    # 1. 1, 3, 5, 7, 9. hanelerin toplamı
    tek_toplam = sum(haneler[0:9:2])

    # 2. 2, 4, 6, 8. hanelerin toplamı
    cift_toplam = sum(haneler[1:8:2])

    # 3. 10. hane ne olmalı?
    beklenen_onuncu = (tek_toplam * 7 - cift_toplam) % 10

    # 4. 11. hane ne olmalı?
    beklenen_on_birinci = sum(haneler[0:10]) % 10

    # 5. İki hane de tutuyorsa True, değilse False dönmeli
    return haneler[9] == beklenen_onuncu and haneler[10] == beklenen_on_birinci