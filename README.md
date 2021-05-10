## Facharbeit zum Thema:
# Vergleich von Listen mit Arrays des Moduls NumPy in Python

In   dieser   Facharbeit   werden   die   Methoden   list.append()   für   Listen   und numpy.append() für Arrays der Programmbibliothek NumPy in Bezug auf Laufzeit- und Speicherentwicklung miteinander verglichen. Beide Methoden können verwendet werden, um Elemente an die dazugehörige Datenstruktur anzuhängen.

Wenn  numpy.append()  aufgerufen   wird,   um   ein   neues   Element   an   das   Array anzuhängen, wird das Array zuerst an eine neue Position im Speicher kopiert und erst dort wird das neue Element angehängt.

Bei der Verwendung von list.append() wird die Liste nur selten kopiert. Das ist unter anderem  darauf   zurückzuführen,  dass  systematisch   Speicherplatz   für  neue   Elemente reserviert wird, sodass dieser nicht durch andere Programmstrukturen blockiert werden kann. Dadurch hat die Liste an ihrer Position genug Platz, um neue Elemente anzuhängen und muss nicht zuerst an einen neuen Ort im Speicher kopiert werden. Erst, wenn die Liste keinen reservierten Platz mehr für neue Elemente hat, wird ihr Speicher erweitert und dabei Platz für neue Elemente freigehalten.

Da   das   Kopieren   einer   Datenstruktur   aufwendig   ist,   beansprucht   die   Methode numpy.append()  in der Regel deutlich mehr Laufzeit als die Methode  list.append(),während der Speicherbedarf der Datenstrukturen dabei relativ ähnlich ist.
