

### Windows + Linux
- Speicher Array (+Bezug auf OS)
    - linear (+8 Bytes)
    - bei beiden Betriebssystemen gleich

    - Bezug Grundlagen

- Speicher Liste (+Bezug auf OS)
    - Wachstum um ca. 1/8 in größer werdenen Perioden
    - bei beiden Betriebssystemen gleich

    - Bezug auf Grundlagen
- Zusammenhang Array + Liste
    - Liste wächst an, wenn Größe x kleiner als bei Array ist

### Windows
- Laufzeit
    - Zeitmessung unpräzise 

    - Vermutung: Beanspruchen von mehr Laufzeit hängt mit Ausführen von mehr Operationen zwischen Zeitmessung zusammen
        -> mehr Operationen -> höhere WK, dass diese tatsächlich zwischen Zeitmessung ausgeführt werden

    - Vermutung 1: keine chronologische Ausführung -> Betriebssystem/Interpreter/Virtuelle Hardware?
    - Vermutung 2: Da keine Zeit beansprucht wird, wird der Wert auf den time.time() zugreift, nicht im Hintergrund aktualisiert

    - Wenn man davon ausgeht, dass Laufzeit mit Anzahl an Operationen zusammenhängt(da WK steigt, dass andere Operationen zwischen Zeitmessung passieren), lässt es darauf schließen, dass Arrays mehr Laufzeit benötigen.
        -> Mehr Operationen durch Neuplatzierung

- Bezug auf Speicher
    - Zusammenhang?

### Linux
- Laufzeit
    - Laufzeitveränderung manchmal 0/ Verschiedene Level bei Laufzeitveränderung
        -> Laufzeit zu klein zum präzisen Messen
            -> Gründe Windows
        -> Unklar ob Messwert Laufzeit oder Ungenauigkeiten der Messung abbildet

    - komische Sprünge (Hintergrundprozesse; aber weniger als bei Windows)

    - Messdaten genauer als bei Windows?
        -> Deutlich mehr Messwerte bei Laufzeitveränderung, die > 0 sind
        -> weniger komische Sprünge

    - Array benötigt deutlich mehr Laufzeit
        -> Mehr Operationen durch Neuplatzierung

    - Bei Listen: Gerade durch Minimale Laufzeitänderung parallel zu X-Achse
        -> Laufzeitveränderung unabhängig von Anzahl der Elementen

    - Bei Array: Gerade durch Minimale Laufzeitänderung steigt ungefähr linear
        -> Laufzeitveränderung proportional zu Anzahl der Elementen
        -> Exponentieller Anstieg der Gesamtlaufzeit
            -> Undeutlich durch Ausnahmefälle



- Bezug auf Speicher
    - Zusammenhang?

### Windows + Linux
- Laufzeitmessung Unterschiede
    - Daten schwer vergleichbar
        -> Zeitmessung unpräzise (manchmal Änderung = 0)
        -> Ausnahmefälle mit extremen Abweichungen

        -> Kann an äußeren Einflüssen liegen
    - Welches Betreibssystem schneller?
