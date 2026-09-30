#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansör Etik İtiraz Komitesi

Bu yazılım, bir asansör düğmesine basılmadan önce
Ulusal Kat Seçimi Etik Kurulu'nun onayını simüle eder.

Çalışır. Yardımcı olur mu? Tartışmalı.
"""

from __future__ import annotations

import base64
import random
import time
from dataclasses import dataclass

GIZLI = base64.b64decode(
    b"QnVyb2tyYXNpIGZvcm1hLCBrYXQgZ2VjIGdlbGl4dGlyLiBNZWNsaXMgdGF0aWxlIGdpcmluY2UgYXNhbnNvciBkYWhhIGhpemxpIGNhbGlzaXIu"
).decode("utf-8")


KARARLAR = [
    "ONAYLANDI: Kat ahlaken kabul edilebilir.",
    "REDDEDİLDİ: Bu kat, kamu vicdanını rahatsız eder.",
    "ERTELENDİ: Kurul çay molasındadır. Lütfen merdiven kullanınız.",
    "ŞARTLI ONAY: Yalnızca kimse sizi görmeden inebilirsiniz.",
    "İNCELEMEDE: Dosyanız 14 iş günü içinde değerlendirilecektir.",
    "MÜKERRER BAŞVURU: Aynı kata günde bir kez başvurulabilir.",
]


GEREKCELER = [
    "Çünkü 7. kat fazla iddialı duruyor.",
    "Çünkü zemin kat zaten yeterince alçaktır.",
    "Çünkü asansör de bir kamu hizmetidir.",
    "Çünkü düğme, toplum sözleşmesinin parçasıdır.",
    "Çünkü merdiven de bir seçenektir ve özgürlüktür.",
    "Çünkü kurul üyelerinden biri o katta oturuyor olabilir.",
]


@dataclass
class KurulKarari:
    kat: int
    metin: str
    gerekce: str
    sure_saniye: float

    def resmi_yaz(self) -> str:
        return (
            f"\n=== ULUSAL KAT SEÇİMİ ETİK KURULU ===\n"
            f"Başvurulan kat : {self.kat}\n"
            f"Karar          : {self.metin}\n"
            f"Gerekçe        : {self.gerekce}\n"
            f"İnceleme süresi: {self.sure_saniye:.1f} saniye\n"
            f"=====================================\n"
        )


def kurul_toplanir(kat: int) -> KurulKarari:
    if kat < -2 or kat > 88:
        return KurulKarari(
            kat=kat,
            metin="YETKİSİZLİK: Bu kat bu binada yok, evrende de tartışmalı.",
            gerekce="Harita müdürlüğüne de başvurunuz.",
            sure_saniye=0.0,
        )
    sure = random.uniform(0.4, 1.8)
    time.sleep(min(sure, 0.6))
    return KurulKarari(
        kat=kat,
        metin=random.choice(KARARLAR),
        gerekce=random.choice(GEREKCELER),
        sure_saniye=sure,
    )


def main() -> None:
    print("Asansör Etik İtiraz Komitesi v0.0.1")
    print("Düğmeye basmadan önce kurul toplanır.\n")
    raw = input("Hangi kata çıkmak istiyorsunuz? (sayı): ").strip()
    try:
        kat = int(raw)
    except ValueError:
        print("Bu bir kat değil, bir duygudur. Reddedildi.")
        return
    karar = kurul_toplanir(kat)
    print(karar.resmi_yaz())
    if "gizli" in raw.lower():
        print("(dipnot)", GIZLI)


if __name__ == "__main__":
    main()
