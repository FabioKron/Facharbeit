# Durchführung

### Informationen

- VM
    - 4096 MB Arbeitsspeicher
    - 1 CPU 

    1. Windows 10 (Nov/2020)
        - Interpreter: 
            - cPython 3.8.8
        - Acceleration: 
            - VT-x/AMD-V
            - Nested Paging
            - Hyper-V Paravirtualization

    2. Ubuntu 20.04.2.0
        - Interpreter: 
            - cPython 3.8.5
        - Acceleration: 
            - VT-x/AMD-V
            - Nested Paging
            - KVM Paravirtualization

- Algorithmus zum Dokumentieren der Laufzeit und des belegten Speichers
(Flussdiagramm)
    - berechnen Laufzeit
    - berechnen Laufzeitveränderung
    - berechnen Speicher
    - berechnen Speicherveränderung

- float ( 0-1)

- Durchführungen: 2 * 50 * 10000 (zum Verringern der Streuung)
- Mittelwert + Maximalabweichung
