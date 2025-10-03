from datetime import datetime
from typing import Optional, List
from enum import Enum

class StatusZadania(Enum):
    Oczekujace = "Oczekujące"
    W_Trakcie = "w_trakcie"
    Zakończone = "Zakończone"

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
        self.data_utowrzenia = data_utworzenia or datetime.now()
