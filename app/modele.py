from datetime import datetime
from typing import Optional, List
from enum import Enum

class StatusZadania(Enum):
    Oczekujace = "Oczekujące"
    W_Trakcie = "w_trakcie"
    Zakonczone = "Zakończone"

class Zadanie:
    def __init__(self,
                 tytul: str,
                 opis: str = "",
                 status: StatusZadania = StatusZadania.Oczekujace,
                 termin: Optional[datetime] = None,
                 data_utworzenia: Optional[datetime] = None,
                 id_zadania: Optional[int] = None):
        self.id_zadania = id_zadania
        self.tytul = tytul
        self.opis = opis
        self.status = status
        self.termin = termin
        self.data_utworzenia = data_utworzenia or datetime.now()

    def na_slownik(self) -> dict:
        slownik = {
            'id_zadania' : self.id_zadania,
            'tytul' : self. tytul,
            'opis' : self.opis,
            'status' : self.status.value,
            'data_utowrzenia' : self.data_utworzenia.isoformat()
        }
        if self.termin:
            slownik['termin'] = self.termin.isoformat()
        else:
            slownik['termin'] = None


    @classmethod
    def ze_slownika(cls, dane: dict) -> 'Zadanie':
        termin = None
        if dane.get('termin'):
            termin = datetime.fromisoformat(dane['termin'])

        return cls(
            id_zadania= dane.get('id_zadania'),
            tytul= dane['tytul'],
            opis= dane.get('opis', ''),
            status= StatusZadania(dane['status']),
            termin= termin,
            data_utworzenia= datetime.fromisoformat(dane['data_utworzenia'])
        )

    def __str__(self) -> str:

        pass
    def czy_przeterminowane(self) -> bool:

        pass
