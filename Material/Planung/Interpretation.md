

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

- Bezug auf Speicher
    - Zusammenhang?

### Linux
- Laufzeit
- Bezug auf Speicher

### Windows + Linux
- Laufzeitmessung Unterschiede