# Quellen und Notizen zur Recherche
---
**Exploring Python’s Implementation of List.append() in C**

Autor geht in Artikel auf den Sourcecode von cpython/Objects/listobject.c ein.
Dabei bezieht er sich unter anderem auf das "Reservieren" von Speicherplatz.

https://lisantra.wordpress.com/2020/04/24/python-internals-list-append/

8.2.2021/8:21

---

**listobject.c Python Quellcode auf Github**

Der Quellcode enthält unter anderem die Implementierung von append in Python.

https://github.com/python/cpython/blob/master/Objects/listobject.c

8.2.2021/8:30

---

**Python Docs How are lists implemented in CPython?**

Es wird kurz darauf eingegangen, dass bei Listen Speicher für die Liste freigehalten wird.

https://docs.python.org/3/faq/design.html#how-are-lists-implemented

8.2.2021/ 9:19

---

**Python Wiki TimeComplexity**

Es wird auf die Zeitkomplexität von Methoden von Listen eingegangen.

https://wiki.python.org/moin/TimeComplexity

8.2.2021/ 9:24

---

**Why is np.append so slow?**

Diskussion auf Github über Numpy.append und List.append.
Es unter anderem erklärt, wie die jeweilige Methode funktioniert.

https://github.com/numpy/numpy/issues/17090

8.2.2021/ 9:28

---

**Numpy Dokumentation numpy.append**

Es wird erwähnt, dass beim anhängen von Elementen der Array an eine andere Stelle im Speicher verschoben wird und erst dort das neue Element angehängt wird.

https://numpy.org/doc/stable/reference/generated/numpy.append.html#numpy.append

9.2.2021/ 8:35

---

## python.org Dokumentation Listen

- Basics:  
    https://docs.python.org/3/tutorial/introduction.html#lists

- Mehr zu Listen:  
    https://docs.python.org/3/tutorial/datastructures.html
    
---
## numpy.org Dokumentation Arrays

-  Array creation:  
        https://numpy.org/doc/stable/user/basics.creation.html

-  Array manipulation routines:
        https://numpy.org/doc/stable/reference/routines.array-manipulation.html

